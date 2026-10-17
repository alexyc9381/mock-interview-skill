import json
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SKILL = os.path.join(ROOT, "skills", "mock-interview", "SKILL.md")


class SkillTest(unittest.TestCase):
    def setUp(self):
        with open(SKILL) as f:
            self.text = f.read()

    def test_frontmatter(self):
        self.assertTrue(self.text.startswith("---\nname: mock-interview\n"))
        for key in ("description:", "argument-hint:", "license: MIT"):
            self.assertIn(key, self.text.split("---")[1])

    def test_command_matches_the_video(self):
        # the reel types: /mock-interview job-post.pdf
        self.assertIn("# /mock-interview", self.text)
        self.assertIn("file path (read it; PDF is fine)", self.text)

    def test_five_claudes(self):
        for who in ("The recruiter", "The hiring manager", "The team lead", "The coach", "The grader"):
            self.assertIn("**%s.**" % who, self.text)

    def test_one_question_at_a_time(self):
        self.assertIn("Ask ONE question. Then stop and wait for the user's answer.", self.text)
        self.assertIn("never grade during the interview", self.text)

    def test_report_and_rewrites(self):
        self.assertIn("## 4. Grade it", self.text)
        self.assertIn("## 5. Rewrite the weakest answers", self.text)
        for f in ("TRANSCRIPT.md", "REPORT.md", "BETTER-ANSWERS.md"):
            self.assertIn(f, self.text)

    def test_never_invents(self):
        self.assertIn("Never invent employers, titles, dates, numbers or results", self.text)

    def test_credit_line(self):
        self.assertIn("Made with /mock-interview by Alex Chen (@nocodealex) · chen.media", self.text)

    def test_plugin_files(self):
        for name in ("plugin.json", "marketplace.json"):
            with open(os.path.join(ROOT, ".claude-plugin", name)) as f:
                data = json.load(f)
            self.assertIn("mock-interview-skill", json.dumps(data))


if __name__ == "__main__":
    unittest.main()
