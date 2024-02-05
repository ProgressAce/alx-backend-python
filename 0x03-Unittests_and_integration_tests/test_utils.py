#!/usr/bin/env python3
"""Test file for utils.py"""

import requests
from unittest import TestCase
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(TestCase):
    """Confirms the desired workings of utils.access_nested_map function."""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, desired_output):
        """Ensure that access_nested_map works with valid arguments."""

        output = access_nested_map(nested_map, path)
        self.assertEqual(output, desired_output)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]  # empty map  # extra key path
    )
    def test_access_nested_map_exception(self, nested_map, path, desired_output):
        """Ensures that a KeyError is raised with these invalid arguments"""

        with self.assertRaises(desired_output):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """Confirms the desired workings of the utils.get_json function."""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, url, desired_output):
        """Ensures that the function works as intended."""

        # create mock object to be used as a return
        mock_response = Mock()
        mock_response.json.return_value = desired_output

        with patch(
            "requests.get", return_value=mock_response.json.return_value
        ) as mock_get:
            response = get_json(url)

            self.assertEqual(response, desired_output)
            mock_get.assert_called_once_with(url)
