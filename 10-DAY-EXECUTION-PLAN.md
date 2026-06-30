# Mission Growth: 10-Day Execution Plan

Source: Astrion Defense Mission Growth Meeting, 2026-06-29 (`Astrion Defense Mission
Growth Meeting-Transcription.md` + summary `.docx`).
Window: Tue 2026-06-30 (Day 1) → reconvene Tue 7/7 or Wed 7/8, execute 7/9.
Owner of this document: Shane Turner.

---

## 1. What the meeting actually decided

Tom closed the meeting by handing the team "a week, 10 days" to stop talking and lock
things down, then reconvene on a date that "becomes the day where that's the plan." Two
hard deliverables come out of that, plus supporting work.

**The two deliverables that decide the reconvene:**

1. **Locked strategy, pursuits, and shaping** — owned by the mission/assault-team leads
   (Dave / Layered Defense, Jake / Autonomous Warfare, Brad / Integrated Fires),
   facilitated by Tom. Must-wins, shaping moves, and essential capabilities, sorted
   across 12-18mo / 24mo / 3-5yr horizons, each with a named senior capture manager.

2. **Astrion Core buildout definition + cost model** — owned by **you and Sully**. This
   is your direct assignment: "lock down what is it they need to actually build out these
   layers, and what's it gonna cost." This is the gating item. The reconvene is won or
   lost here.

**Supporting commitments:** Con/Rob adjust the mission strategy & pipeline deck and fold
it into the market strategy brief; a daily stand-up runs the sprint; the reconvene gets
scheduled around Dave's 7/9 travel.

### The strategic goals this 10-day work serves

- Protect and expand existing franchises (counter-UAS beyond the IFRCO recompete; Navy
  autonomous maritime; Army joint fires) while going global, not Army- or US-centric.
- Sell **turnkey mission packages** (platforms, C2, effectors, sensors), not individual
  hardware. Be hardware-independent: "we don't build the drone, we provide the turnkey
  autonomous solution."
- Build **Astrion Core** as one common orchestration / integration / data-fabric platform
  across all verticals, with mission "engines" running on top. Not three stacks.
- Own counter-UAS ranges globally and the data they generate (Muscle Shoals as the
  repeatable proof point).
- Win must-wins with senior capture leadership (NUS/AFRL is the named ~$500M must-win).
- Prove Astrion is no longer a "bucks-and-seats service company" by getting MVPs into
  operations by EOY-2026, which gates the ~$450-500M raise (socialize spring 2027).

---

## 2. How to accomplish the goals

The goals are large and multi-year, but the 10-day job is narrow: convert intent into a
**costed, prioritized, defensible plan** the leadership can fund. Five moves get you there.

**Move 1 — Treat the Core cost model as the critical path, because it is.** It is the one
deliverable assigned to you, it gates the reconvene, and it is blocked on numbers that
live in other people's heads (Julian's SAG headcount, Rob's AWS/Azure price models, Sean's
Flex number). Extract those inputs in the first three days or the whole thing slips.

**Move 2 — Decide the architecture early.** The cloud-vs-on-prem baseline question is not
a quick fork. Sully already believes one common baseline is not achievable (likely 2,
maybe 3). That decision drives cost, configuration-management burden, and staffing, so
force it by Day 4, before the holiday weekend goes dark.

**Move 3 — Present choices, not one number.** Tom said an $85M ask "is going to be hard,"
funding is bootstrap money, and Berger has to adjudicate across all six missions. Bring
**at least two COAs** (three is too much for this window), a recommended one, a phased
3/6/9-month seat projection, and explicit cut-line choices. A single maximalist number
gets cut arbitrarily. "Cannot be peanut butter."

**Move 4 — Anchor the ask in the value benchmark.** Your strongest card: Northrop needed
~$26M and a 100-person IPT to do what your 3-person team stood up for ~$40-49K. Tom's own
framing is that ~$54M of investment would justify giving Sully four people. Lead the cost
narrative with that comparison.

**Move 5 — Make the mission leads feed you, not the reverse.** Tom was explicit: leads
tell you and Sully what they need; you go get it. Their capture managers, BD plans, and
resource asks are **inputs** to your cost roll-up, so force them to land by Day 6, before
you freeze the model on Day 7.

---

## 3. The 10-day step-by-step process

Reality check baked into the schedule: it is effectively ~7 working days, because **Sat
7/4 (Independence Day) and Sun 7/5 are dark**, and Dave travels starting 7/9 so the
reconvene must land on 7/7 or 7/8 with almost no slack. Every externally-owned number must
be in hand by close of business Friday 7/3.

Daily stand-up (you + Rob + Dave, Sully on the Core line), 15-30 min, every working day.
Each stand-up forces one decision and produces one artifact. No weekend stand-ups.

| Day | Date | Theme | Gate / exit |
|-----|------|-------|-------------|
| 1 | Tue 6/30 | **Kickoff.** You transition off business-unit work to product full-time (hand off to Sean/Joe); stand up the daily cadence; book tomorrow's seat-data meeting (Julian in, Sharon out); ping every cost-model input owner; draft the deliverable skeleton; leads start the strategy debate; Con/Rob own the deck. | Every unknown has a named owner and is pinged; cadence on calendars. |
| 2 | Wed 7/1 | **GATE A — inputs + architecture frame.** Hold the seat-data meeting (roll up dev counts across Sully's ~10, Julian/SAG, SET-FL, SET-MD, Pasadena, Flex; park the plus-up); Rob confirms the price-model harness + tiers; Sully drafts the Core layer + baseline question; leads open NUS/CAMEL/Layered-Defense work. | Named owner + hard deadline on every input; draft Core+baseline definition; unowned inputs escalated *today*. |
| 3 | Thu 7/2 | **GATE 1 — seat number locked.** Julian delivers the SAG headcount (or a firm time); finalize the rolled-up seat number + plus-up. **Fallback: if Julian is late, proceed on a documented assumption and escalate to Con — do not wait.** Lock licensing tiers + enterprise floor (~100; internal 151); Con/Rob pull the deck baseline; **order the NVIDIA chips**; leads produce draft must-win lists with named capture managers. | GATE 1 GO. |
| 4 | Fri 7/3 | **GATE B/C — kill the fork, build COAs, first numbers before the holiday.** Lock the baseline decision; build ≥2 costed COAs with the phased 3/6/9-month projection; Rob runs the price models; lock the staffing model (Core infra team + dedicated, non-matrixed SEG mission-app dev teams, embedded early); characterize the software-to-hardware construct (LOC, chips, power). | Baseline LOCKED; two costed COAs; first end-to-end numbers; **every externally-owned number physically in hand.** |
| 5 | Sat 7/4 | **DARK — Independence Day.** No stand-up, no decisions. Optional async drop of late data. You post a short check-in + the weekend synthesis task. | No deliverable. |
| 6 | Sun 7/5 | **DARK — solo synthesis (async).** You assemble the Core deliverable draft: final seat number + plus-up into both COAs, Rob's cost figures attached, baseline rationale + value-for-money narrative. Post Sunday evening. | Draft Core deliverable with two costed COAs posted. |
| 7 | Mon 7/6 | **GATE 2 — freeze the cost model + judicious-cut pass.** Two COAs costed end-to-end, baseline decided, tiers + plus-up locked, single rolled-up figure, discount threshold marked. Run the cut-line pass vs $85M; identify MVPs for EOY-2026 (Navy OTA payload integration, Army HMT RPP); Con/Rob assemble the integrated deck; leads deliver near-final must-wins. | GATE 2 GO. |
| 8 | Tue 7/7 | **Final assembly + GATE 3 dry-run** (primary reconvene window opens). Assemble both deliverables; dry-run to Tom/Eric/Con; pressure-test the ask; Berger reviews for cross-mission trimming. If clean, hold the reconvene today; else fix overnight for 7/8. | Both deliverables assembled; dry-run passed or gaps captured; reconvene confirmed. |
| 9 | Wed 7/8 | **RECONVENE — it becomes the plan.** Leads present locked strategy with named capture managers; you + Sully present the Core buildout + costed model with the prioritized ask and cut-line choices; Con/Rob present the integrated brief; Tom/Berger adjudicate across six missions and confirm MVP-by-EOY tied to the raise. Capture decisions in writing. | The plan is locked, before Dave's travel. |
| 10 | Thu 7/9 | **Execute.** Dave departs (no dependency on him); Sully begins standing up the Core cloud instance + seat provisioning; form the SEG mission-app dev teams; start NVIDIA experimentation; advance the site visit; log open decisions with owners; confirm raise checkpoints. | Execution started against the locked, funded plan. |

---

## 4. Critical risks and the gaps to close (from adversarial review)

These came out of stress-testing the plan against the transcript. Several were missing
from the obvious version of the plan.

**Top risks to manage:**

- **The cost model is hostage to one input** (Julian's SAG headcount). Mitigation:
  documented seat assumption by Day 3, escalate, never wait.
- **~7 working days, not 10**, and zero back-end slack before Dave's 7/9 travel. A failed
  7/7 dry-run leaves only 7/8.
- **The ask will likely exceed appetite.** Without explicit cut-line choices and a
  recommended COA, the Core ask gets cut for you.
- **Multiple Core baselines** drive cost and CM burden, and the technical definition of
  Core (chips, power, architecture, LOC) is still soft.
- **The 3-person Core team cannot build mission applications.** You can only *plan and
  cost* the dedicated SEG dev teams in this window, not stand them up.
- **Don't lean MVP claims on Muscle Shoals** — land isn't purchased, gated by certificate
  of occupancy and data-permission constraints. Lean on the Navy OTA and Army HMT RPP.

**Must-add items the first-pass plan missed:**

1. Assign an owner (Eric, with you/Sully) to answer **"what exactly are we taking to
   market where services are insufficient?"** DIU/DARPA won't buy services. This is the
   biggest strategic gap.
2. Surface the **HMT acquire-vs-build decision** (Havoc AI or similar). SEG likely lacks
   the competency in-house; it changes Jake's staffing and cost.
3. Force the **mission-lead resource asks to land before the cost freeze** (Day 6), since
   the cost model rolls them up.
4. Produce a **bootstrap-reality funding view**: what bootstrap dollars fund toward
   EOY-2026 MVPs vs what needs the raise.
5. Give the **in-person assault-team skill-set site visit** a real date and owner.
6. Produce **first-cut Core technical numbers** (LOC, chips, power) — Tom asked, and
   DIU/DARPA interest hinges on the deliverable hardware.

---

## 5. The tool to monitor progress

**Recommendation: track the sprint in your existing Jira AI Program space (`AIPROG`),
populated automatically from the meeting analysis.** You already have the board and the
sibling spaces (AI Data Foundation, AI Executive Dashboards, CORE, Enterprise Platform
Roadmap). A standalone tracker would just compete with it. The AI's job is to *populate
and keep it in sync*, not replace it.

The structured backlog is committed in `jira/backlog.json` and turns into Jira issues
three ways (details in `jira/README.md`):

- **CSV import** — `jira/jira_import.csv`, drop into Jira's importer. No credentials.
- **REST API script** — `python3 jira/populate_jira.py --create`. Repeatable, re-syncable.
- **Rovo connector** — Claude creates the issues directly once the connector is granted
  access to the `astrioninnovation.atlassian.net` site (currently blocked pending that
  grant; see the README).

**What gets created:** 6 Epics → 29 Tasks → 10 Sub-tasks (the day-by-day schedule).

| Epic | Covers |
|------|--------|
| Astrion Core Buildout & Cost Model **(gating)** | layer definition, baseline decision, seat roll-up, price models, ≥2 COAs, staffing, value benchmark, edge-AI |
| Strategy, Pursuits & Shaping Lockdown | per-vertical must-wins; HMT decision; go-to-market offering |
| Must-Win Captures | NUS/AFRL senior CM, CAMEL re-entry |
| Deck → Market Strategy Brief | deck adjust + lily-pad linkage |
| MVP & Funding Readiness | EOY-2026 MVPs, bootstrap/cut-line view, raise checkpoints |
| Sprint Cadence, Logistics & 10-Day Schedule | stand-up, seat meeting, reconvene scheduling, site visit, the 10 days |

**What to watch on the board:**

- **Gating banner** — the Core/cost epic and its `gating`-labelled tasks should hit Done
  by Day 8. Filter `labels = gating`.
- **Blocked/dependency items** — especially the seat-count inputs from Julian/Rob/Sean.
  Anything still open at Day 3 is a schedule risk.
- **Day burndown** — the 10 sub-tasks (D1–D10) give a clean day-by-day view; gates sit at
  D3, D7, D8.
- **Owner load** — your own load (Core + transition + stand-up) is the capacity risk;
  watch for unassigned capture-manager slots.
- **Cut-line indicator** — when COA totals exist, flag any that cross the $85M caution.

This same board, with refreshed dates, becomes the recurring mission-growth cadence board
after the reconvene.
