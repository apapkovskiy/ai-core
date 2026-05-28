#!/usr/bin/env python3
"""Convert Kinopoisk 10-point rating to Notion Score/5."""

from __future__ import annotations

import argparse


def to_score_5(score_10: float, integer_only: bool = False) -> float | int:
    """Convert a 10-point rating to a 5-point score.

    Args:
        score_10: Rating on a 0-10 scale.
        integer_only: Return nearest integer if True.

    Returns:
        Score on a 0-5 scale, rounded to one decimal (or int).
    """
    if not 0 <= score_10 <= 10:
        raise ValueError("score_10 must be between 0 and 10")

    score_5 = round(score_10 / 2, 1)
    if integer_only:
        return int(round(score_5))
    return score_5


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert Kinopoisk score (0-10) to Notion Score/5"
    )
    parser.add_argument("score_10", type=float, help="Kinopoisk score on 0-10 scale")
    parser.add_argument(
        "--integer-only",
        action="store_true",
        help="Return nearest integer for Notion number properties without decimals",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    print(to_score_5(args.score_10, integer_only=args.integer_only))


if __name__ == "__main__":
    main()
