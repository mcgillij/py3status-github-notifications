# -*- coding: utf-8 -*-
"""
Module to display your Github notifications
"""
from github import Github, GithubException


class Py3status:
    cache_timeout = 300
    format = " {notifications}"
    gh_token = "put your token here"

    def _get_notifications(self):
        try:
            return Github(self.gh_token).get_user().get_notifications().totalCount

        except GithubException as github_exception:
            print(f"error {github_exception}")
            raise

    def github_notifications(self):
        notifications = self._get_notifications()
        full_text = self.py3.safe_format(self.format, {"notifications": notifications})
        if notifications and notifications > 0:
            color = self.py3.COLOR_BAD
        else:
            color = self.py3.COLOR_GOOD
        return {
            "full_text": full_text,
            "cached_until": self.py3.time_in(self.cache_timeout),
            "color": color,
        }


if __name__ == "__main__":
    from py3status.module_test import module_test

    module_test(Py3status)
