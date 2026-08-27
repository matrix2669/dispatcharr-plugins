import unittest

from scripts.validate_registry import (
    ValidationError,
    archive_ref,
    requires_local_detail_validation,
    validate_version,
)


class VersionValidationTests(unittest.TestCase):
    def test_dev_accepts_beta_and_completed_stable_versions(self):
        validate_version("1.2.0-beta.3", "dev", "test")
        validate_version("1.2.0", "dev", "test")

    def test_main_rejects_beta_version(self):
        with self.assertRaises(ValidationError):
            validate_version("1.2.0-beta.3", "main", "test")

    def test_main_accepts_normal_semantic_version(self):
        validate_version("1.2.0", "main", "test")


class ArchiveValidationTests(unittest.TestCase):
    def test_accepts_semantic_tag_and_full_commit(self):
        self.assertEqual(
            archive_ref("https://api.github.com/repos/example/plugin/zipball/v1.2.0-beta.3", "test"),
            "v1.2.0-beta.3",
        )
        commit = "a" * 40
        self.assertEqual(
            archive_ref(f"https://api.github.com/repos/example/plugin/zipball/{commit}", "test"),
            commit,
        )

    def test_rejects_moving_branch(self):
        with self.assertRaises(ValidationError):
            archive_ref("https://api.github.com/repos/example/plugin/zipball/dev", "test")


class DetailManifestValidationTests(unittest.TestCase):
    def test_dev_reusing_main_does_not_validate_stale_local_detail(self):
        self.assertFalse(requires_local_detail_validation("dev", "main"))

    def test_same_channel_detail_is_validated_locally(self):
        self.assertTrue(requires_local_detail_validation("dev", "dev"))
        self.assertTrue(requires_local_detail_validation("main", "main"))


if __name__ == "__main__":
    unittest.main()
