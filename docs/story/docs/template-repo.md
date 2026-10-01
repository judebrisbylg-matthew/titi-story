# Template Repo Guide

This repository is intentionally structured so it can be reused as a template for future Codex story-writing skills.

## What Makes It Reusable

The repo separates five concerns:

1. the skill instructions
2. the agent metadata
3. the domain rules
4. the production workflow docs
5. the example outputs

That separation makes it easier to adapt the project without mixing permanent skill logic with one-off story content.

## What To Replace For A New Character Skill

If you want to turn this into a new children’s story skill for another IP, replace these parts first:

### 1. Skill identity

- `skills/titi-story/`
- skill name in `SKILL.md`
- display name in `agents/openai.yaml`
- command name used in prompts

### 2. Character lock

Replace:

- protagonist name
- appearance rules
- costume rules
- day/night version rules
- prop rules

### 3. World logic

Replace:

- `愿望灯` rules
- magic boundaries
- tone constraints
- educational constraints

### 4. Output structure

Replace only if the new production pipeline truly needs a different format.

If the workflow is still:

`word -> script -> storyboard -> image prompts -> dubbing -> edit`

then keeping the existing structure is usually better.

### 5. Examples and docs

Update:

- `README.md`
- `docs/*.md`
- `examples/*.md`
- source reference files

## Recommended Fork Strategy

For the next related project, the clean path is:

1. duplicate this repo
2. rename it to the new series or skill name
3. duplicate `skills/titi-story` into the new skill folder
4. replace only the domain-specific rules first
5. keep the structural parts until real workflow differences appear

## What Not To Change Casually

Do not casually change:

- section order
- four 15-second blocks of three continuous frames, with a two-row-by-six-column board
- learning intro block
- dialogue summary pattern
- smart matching line

Those are the parts that make downstream production predictable.

## Minimum Files For A Derived Skill Repo

At minimum, keep these files:

- `README.md`
- `skills/<skill-name>/SKILL.md`
- `skills/<skill-name>/agents/openai.yaml`
- `docs/install.md`
- `docs/workflow.md`
- `docs/example-output.md`
- `CHANGELOG.md`

## When To Split A New Repo Instead Of Reusing This One

Start a separate repo if:

- the target age range changes significantly
- the story format is not bilingual anymore
- the episode production structure is no longer four continuous 15-second blocks
- the output is no longer aimed at animated short-form production
- the character/world rules differ enough that almost every paragraph must be rewritten
