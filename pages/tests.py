from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        r = self.client.get("/")
        self.assertEqual(r.status_code, 200)

    def test_url_available_by_name(self):
        r = self.client.get(reverse("home"))
        self.assertEqual(r.status_code, 200)

    def test_template_available_by_name(self):
        r = self.client.get(reverse("home"))
        self.assertTemplateUsed(r, "home.html")

    def test_template_content(self):
        r = self.client.get(reverse("home"))
        self.assertContains(r, "<h1>Homepage</h1>")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        r = self.client.get("/about/")
        self.assertEqual(r.status_code, 200)

    def test_url_available_by_name(self):
        r = self.client.get(reverse("about"))
        self.assertEqual(r.status_code, 200)

    def test_template_available_by_name(self):
        r = self.client.get(reverse("about"))
        self.assertTemplateUsed(r, "about.html")

    def test_template_content(self):
        r = self.client.get(reverse("about"))
        self.assertContains(r, "<h1>About page</h1>")
