---
name: design-router
description: "Select and combine design skills for building or reviewing web interfaces: landing pages, SaaS workspaces, dashboards, admin screens, forms, tables and monitoring. Excludes backend-only tasks and native Figma editing."
license: MIT
---

# Design router

Route by the user's goal and the screen's job, not by words such as “page”, “SaaS” or “dashboard” alone. This is an instruction-based router, not a runtime classifier or permission to expand the task.

## Choose a small working set

1. Identify the requested surface and whether it is public acquisition, daily product work, analysis, administration, or operations. For a component edit, keep the scope at component level.
2. Read [design-core](../design-core/SKILL.md) once for shared foundations, states and verification.
3. Choose the primary specialist below. Add only specialists whose responsibilities actually occur in the requested work. Read their `SKILL.md` files directly if the agent has no nested skill invocation feature. Resolve these paths relative to this file, not the project working directory.
4. State a short route, for example: `design-core → web-app-design + data-table-design; task: workflow runs`. Then implement or review as requested; routing is not the deliverable.

| User intent | Primary specialist | Add when needed |
|---|---|---|
| Explain an offer, acquire leads, sell a product | [landing-page-design](../landing-page-design/SKILL.md) | forms-settings for a substantial signup flow, not for a single email field |
| Complete daily work: inbox, editor, projects, workflow runs | [web-app-design](../web-app-design/SKILL.md) | tables, forms, monitoring only for their respective areas |
| Understand trends, compare performance, investigate metrics | [dashboard-design](../dashboard-design/SKILL.md) | web-app-design if building a new app shell; data-table-design for drill-down records |
| Manage users, roles, resources, privileged CRUD | [admin-panel-design](../admin-panel-design/SKILL.md) | web-app-design for a new shell; tables for lists; forms for editing |
| Enter information, configure preferences, save settings | [forms-settings](../forms-settings/SKILL.md) | web-app-design only when the surrounding shell is also in scope |
| Search, compare, select, sort or act on records | [data-table-design](../data-table-design/SKILL.md) | admin-panel-design only for privileged operations |
| Triage live health, alerts, incidents, logs | [monitoring-ui](../monitoring-ui/SKILL.md) | dashboard-design for analytical charts; tables for incident/log lists |

For a whole product, route each surface separately under one shared brand. Do not apply landing-page composition to authenticated work. Do not add a dashboard solely because an app has a sidebar or a statistic.

## Ambiguity and boundaries

- “SaaS homepage” can mean public marketing or the signed-in home screen. Inspect routes, screenshots and nearby code. Ask one short question only if that distinction remains material; otherwise state the assumption and proceed.
- A “billing dashboard” that mainly edits a card is a forms task; one that analyzes revenue is analytics. The main action decides.
- Fixing a table sort bug needs table interaction checks, not a new brand, shell or marketing story.
- Backend jobs, API-only tasks and prose-only tasks do not activate this suite. A Figma-only task uses the separately preserved `figma-designer` skill and its required tooling; do not load its fixed visual rules into web implementation.
- A direct specialist invocation skips this routing step and still loads core once. Never make specialists call the router back.

## Composition contract

User requirements and applicable repository instructions take priority. Reuse the product's established components and brand. Core owns shared quality; specialists own local decisions. A specialist can refine a pattern (for example a scrollable data table), but cannot silently drop keyboard access, readable contrast or recovery from failure. If requirements conflict, explain the concrete conflict and choose a compatible alternative or ask when the decision is consequential.

Install the suite as sibling directories. If a referenced skill is missing, report its exact name and continue with available guidance when possible; do not pretend to have read it or fetch unrelated skills automatically.

## Route checks

| Request | Expected working set |
|---|---|
| “Сделай лендинг SaaS для планирования смен” | core + landing |
| “Экран запусков автоматизаций, фильтры и детали” | core + web-app + table |
| “Управление участниками, роли и приглашение” | core + admin + table + forms; app only for a new shell |
| “Аналитика удержания за квартал” | core + dashboard |
| “Статус сервисов, инциденты и живые логи” | core + monitoring + table |
| “Исправь валидацию формы в существующем экране” | core + forms; preserve shell and brand |
| “Добавь серверный cron без UI” | no design skills |

The shorthand above refers to the full skill names in the routing table. Automatic selection depends on the host agent; explicit invocation is the fallback, not a separate ruleset.
