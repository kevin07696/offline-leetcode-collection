package regexhard_test

import (
	regexhard "regex_hard"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsMatch(t *testing.T) {
	testCases := []struct {
		title   string
		word    string
		pattern string
		isMatch bool
	}{
		{
			title:   "Test_SimpleCharMatching_ReturnsTrue",
			word:    "abc",
			pattern: "abc",
			isMatch: true,
		},
		{
			title:   "Test_SimpleCharMatching_ReturnsFalse",
			word:    "aaa",
			pattern: "a",
			isMatch: false,
		},
		{
			title:   "Test_AnyChar_ReturnsTrue",
			word:    "abc",
			pattern: "ab.",
			isMatch: true,
		},
		{
			title:   "Test_AnyChar_ReturnsFalse",
			word:    "ab",
			pattern: "a..",
			isMatch: false,
		},
		{
			title:   "Test_PatternFinishesFirst_ReturnsFalse",
			word:    "aaaab",
			pattern: "a*",
			isMatch: false,
		},
		{
			title:   "Test_StringFinishesFirst_ReturnsTrue",
			word:    "aaaa",
			pattern: "a*",
			isMatch: true,
		},
		{
			title:   "Test_StringFinishesFirst_ReturnsFalse",
			word:    "aaaa",
			pattern: "a*b",
			isMatch: false,
		},
	}

	for _, tc := range testCases {
		t.Run(tc.title, func(t *testing.T) {
			isMatch := regexhard.IsMatch(tc.word, tc.pattern)

			assert.Equal(t, tc.isMatch, isMatch)
		})
	}
}


