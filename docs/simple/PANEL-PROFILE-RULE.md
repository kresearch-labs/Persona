<div align="center">

# 🎚️ PANEL PROFILE RULE

**Which Panel depth for which model tier**

</div>

<p align="center"><sub>📄 The original text — for readers who want every detail, and the version agents follow: <a href="../../PANEL-PROFILE-RULE.md">read it here</a></sub></p>

> [!IMPORTANT]
> **Finding:** the Panel's structured briefing (per-seat sections, WARNINGS, done-signals, abstention notes) is only an advantage when the host model has the reasoning capacity to parse it. On a speed-tier model the same structure consumes task capacity and **accuracy DROPS**. Right-size the briefing to the model — **never one fixed depth for all.**

---

## 📏 RULE

<table>
<tr>
<th width="50%">⚡ Flash-tier / speed-optimized models</th>
<th width="50%">🧠 Frontier / reasoning models</th>
</tr>
<tr>
<td valign="top">

*GLM-5.3 Flash, and any model tier optimized for speed/cost over reasoning depth*

- ▶️ Run the panel in **`flash`** profile
- 📏 Tight precedent stack: **~18 lines** total across all seats
- 🧹 Keep the flat, simple format — minimal meta-structure
- 👀 The model should see: the relevant precedent, briefly. Nothing to dig through.

</td>
<td valign="top">

*Claude Opus class, GPT-5-class "Sol", DeepSeek Pro class, and future deep-reasoning tiers*

- ▶️ Run the panel in **`full`** profile
- 📏 Complete structured briefing: **~38 lines**, all organs — per-seat headers, WARNINGS (verified-failure runs), WHAT-DONE-LOOKS-LIKE (done-signals), abstention notes, guard caps
- 🎯 The model parses the meta-structure without effort, extracts the signals cleanly, applies them as intended, and still has full capacity for the task

</td>
</tr>
<tr>
<td valign="top">

> 📊 **Rationale (measured):** a 30-38-line structured briefing + a hard task exceeded the Flash model's effective attention — the meta-structure consumed capacity that should have gone to the task, producing well-organized but wrong answers.

</td>
<td valign="top">

> 🎓 **Analogy:** a senior expert given a 30-page briefing extracts exactly what is needed in two minutes and walks in better prepared than someone with no briefing. A junior gets lost in the structure.

</td>
</tr>
</table>

---

## ⚙️ HOW IT'S SET

| Variable | Values |
|---|---|
| `AURA_PB_PANEL_PROFILE` | `flash` (default) \| `full` |
| `AURA_PB_GROUND_BUDGET` | optional direct override of the line count (profile default: flash = 18, full = 38) |
| `AURA_PB_PANEL_PROFILE_DEFAULT` | bakes the env default, for a deployment that always uses a frontier model |

Set per host — e.g. export the profile in the launcher that runs the big model; `flash` stays the default everywhere else.

---

## ⚖️ WHY THIS IS A LAW, NOT A PREFERENCE

The Panel's value is precedent retrieval — the right lived experience in front of the model. But value is delivered only if the model can use it.

> [!WARNING]
> **The briefing document that a model cannot digest is worse than no briefing:** it actively displaces task reasoning.

<div align="center">

### 🎯 Match the briefing to the reader.

</div>
