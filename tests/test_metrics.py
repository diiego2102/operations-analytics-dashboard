import importlib.util
from pathlib import Path
import sqlite3
import unittest

root=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('pipeline',root/'pipeline.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)


class MetricsTests(unittest.TestCase):
    def test_weighted_denominator_and_review_flag(self):
        rows=[dict(day='2026-09-30',asset_id='A',region='North',provider='Alpha',expected=100,received=100,invalid=10,incident=1),
              dict(day='2026-09-30',asset_id='B',region='North',provider='Beta',expected=200,received=100,invalid=0,incident=1)]
        con=p.database(rows); data=p.extract(con);all_row=data['overview'][0]
        self.assertAlmostEqual(all_row['completeness'],200/300)
        self.assertAlmostEqual(all_row['validity'],190/200)
        self.assertEqual(all_row['assets'],2)
        self.assertEqual(all_row['incident_days'],2)
        self.assertAlmostEqual(sum(r['received'] for r in data['overview'][1:]),all_row['received'])
        con.close()

    def test_unique_grain_and_constraint(self):
        row=p.generate()[0];con=p.database([row])
        with self.assertRaises(sqlite3.IntegrityError):
            con.execute('INSERT INTO readings VALUES (:day,:asset_id,:region,:provider,:expected,:received,:invalid,:incident)',row)
        with self.assertRaises(sqlite3.IntegrityError):
            con.execute('INSERT INTO readings VALUES (:day,:asset_id,:region,:provider,:expected,:received,:invalid,:incident)',dict(row,asset_id='bad',invalid=999))
        con.close()

    def test_generator_reproducibility_and_injected_outage(self):
        rows=p.generate();self.assertEqual(rows,p.generate())
        self.assertEqual(len(rows),10800)
        outage=[r for r in rows if r['region']=='South' and r['provider']=='Beta' and '2026-09-11'<=r['day']<='2026-09-15']
        self.assertEqual(len(outage),100)
        self.assertTrue(all(r['received']<60 and r['incident']==1 for r in outage))


if __name__=='__main__':unittest.main()
