from pathlib import Path
import json
import tempfile
import unittest
import export_snapshot

class ExportParity(unittest.TestCase):
    def test_published_snapshot_matches_source(self):
        self.assertTrue(export_snapshot.verify())

    def test_changed_data_blocks_stale_export(self):
        artifact=json.loads((export_snapshot.ROOT/'artifact.json').read_text())
        artifact['snapshot']['datasets']['overview'][0]['assets']+=1
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'artifact.json';path.write_text(json.dumps(artifact))
            with self.assertRaisesRegex(ValueError,'Stale HTML'):
                export_snapshot.verify(path)
