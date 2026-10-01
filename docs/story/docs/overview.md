# Overview

`TiTi Story` is a specialized writing skill for building children's English animation scripts around the original puppet character `提提 (TiTi)`.

The skill is not a general story generator. It is a constrained production skill.

It exists to reliably output one exact story format again and again so the user can move from:

`core word -> script -> storyboard -> image prompts -> dubbing -> final edit`

without re-explaining the production structure each time.

## Core Goal

Produce scripts that are:

- stable in format
- easy to visualize
- easy to dub
- easy to turn into 9:16 animated content
- appropriate for children around ages 3-6

## Core Constraints

- one episode = one core word
- one fixed protagonist
- one fixed magic lantern rule system
- four consecutive 15-second blocks, three 9:16 frames each, in a 16:9 two-row-by-six-column board
- one fixed learning intro sequence
- complete bilingual records across five playback segments, with a separately filtered English matching text

The 8-second learning intro and up-to-8-second repeat-along are separate from the 60-second main story; greeting and farewell are additional. Main shots have motivated camera direction, while teaching shots stay stable. Current output order and rules: [skill](../skills/titi-story/SKILL.md), [output format](../skills/titi-story/references/output-format.md).

## Intended User

This skill is for a creator building serialized children's English listening videos with:

- a recurring main character
- a recurring visual world
- simple English
- stable educational pacing
- high consistency between episodes
