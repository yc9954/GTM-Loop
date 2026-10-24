# 전체 디렉터리 지도

Git으로 추적 중인 파일이 들어 있는 실제 디렉터리를 재귀적으로 표시했다. 로컬 실행 기록·캐시·의존성 폴더는 제외한다. 폴더 구조이며 자동화 구현 상태를 의미하지 않는다. 주요 파일과 59개 스킬의 역할 분류는 [README](../README.md#폴더-구조)를 참고한다.

```text
GTM-Loop/
├── .agents/
│   └── plugins/
├── .claude-plugin/
├── .codex-plugin/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE/
│   ├── scripts/
│   └── workflows/
├── bundles/
├── docs/
│   ├── assets/
│   └── soban-tales/
├── scripts/
├── skills/
│   ├── ab-testing/
│   │   ├── evals/
│   │   └── references/
│   ├── ad-creative/
│   │   ├── assets/
│   │   ├── evals/
│   │   └── references/
│   ├── ads/
│   │   ├── evals/
│   │   └── references/
│   ├── ai-seo/
│   │   ├── evals/
│   │   └── references/
│   ├── analytics/
│   │   ├── evals/
│   │   └── references/
│   ├── aso/
│   │   ├── evals/
│   │   └── references/
│   ├── attribution/
│   │   ├── evals/
│   │   └── references/
│   ├── churn-prevention/
│   │   ├── evals/
│   │   └── references/
│   ├── co-marketing/
│   │   ├── evals/
│   │   └── references/
│   ├── cold-email/
│   │   ├── evals/
│   │   └── references/
│   ├── community-marketing/
│   │   ├── evals/
│   │   └── references/
│   ├── competitor-profiling/
│   │   ├── evals/
│   │   └── references/
│   ├── competitors/
│   │   ├── evals/
│   │   └── references/
│   ├── content-strategy/
│   │   ├── evals/
│   │   └── references/
│   ├── conversion-tracking/
│   │   ├── assets/
│   │   │   ├── gtm-recipes/
│   │   │   │   ├── detect/
│   │   │   │   └── send/
│   │   │   └── snippets/
│   │   ├── evals/
│   │   ├── references/
│   │   └── scripts/
│   ├── copy-editing/
│   │   ├── evals/
│   │   └── references/
│   ├── copywriting/
│   │   ├── evals/
│   │   └── references/
│   ├── cro/
│   │   ├── evals/
│   │   └── references/
│   ├── customer-research/
│   │   ├── evals/
│   │   └── references/
│   ├── directory-submissions/
│   │   ├── evals/
│   │   └── references/
│   ├── emails/
│   │   ├── evals/
│   │   └── references/
│   ├── events/
│   │   ├── evals/
│   │   └── references/
│   ├── footage-repurposing/
│   │   ├── references/
│   │   └── scripts/
│   ├── free-footage-sourcing/
│   │   ├── references/
│   │   └── scripts/
│   ├── free-tools/
│   │   ├── evals/
│   │   └── references/
│   ├── ga-performance-review/
│   ├── gtm-cycle-review/
│   │   ├── assets/
│   │   ├── references/
│   │   └── scripts/
│   ├── image/
│   │   ├── evals/
│   │   └── references/
│   ├── influencer-marketing/
│   │   ├── evals/
│   │   └── references/
│   ├── launch/
│   │   ├── evals/
│   │   └── references/
│   ├── lead-magnets/
│   │   ├── evals/
│   │   └── references/
│   ├── link-building/
│   │   ├── evals/
│   │   └── references/
│   ├── marketing-council/
│   │   ├── evals/
│   │   └── references/
│   │       └── advisors/
│   ├── marketing-ideas/
│   │   ├── evals/
│   │   └── references/
│   ├── marketing-loops/
│   │   ├── evals/
│   │   └── references/
│   ├── marketing-plan/
│   │   ├── evals/
│   │   └── references/
│   ├── marketing-psychology/
│   │   ├── evals/
│   │   └── references/
│   ├── meta-library-research/
│   ├── offers/
│   │   ├── evals/
│   │   └── references/
│   ├── onboarding/
│   │   ├── evals/
│   │   └── references/
│   ├── paywalls/
│   │   ├── evals/
│   │   └── references/
│   ├── popups/
│   │   ├── evals/
│   │   └── references/
│   ├── pricing/
│   │   ├── evals/
│   │   └── references/
│   ├── product-marketing/
│   │   ├── evals/
│   │   └── references/
│   ├── programmatic-seo/
│   │   ├── evals/
│   │   └── references/
│   ├── prospecting/
│   │   ├── evals/
│   │   └── references/
│   ├── public-relations/
│   │   ├── evals/
│   │   └── references/
│   ├── referrals/
│   │   ├── evals/
│   │   └── references/
│   ├── revops/
│   │   ├── evals/
│   │   └── references/
│   ├── sales-enablement/
│   │   ├── evals/
│   │   └── references/
│   ├── schema/
│   │   ├── evals/
│   │   └── references/
│   ├── seo-audit/
│   │   ├── evals/
│   │   └── references/
│   ├── signup/
│   │   ├── evals/
│   │   └── references/
│   ├── site-architecture/
│   │   ├── evals/
│   │   └── references/
│   ├── sms/
│   │   ├── evals/
│   │   └── references/
│   ├── social/
│   │   ├── evals/
│   │   └── references/
│   ├── video/
│   │   ├── assets/
│   │   ├── evals/
│   │   └── references/
│   ├── video-direction/
│   │   └── references/
│   └── video-shotcraft/
│       ├── .claude-plugin/
│       ├── .github/
│       │   ├── ISSUE_TEMPLATE/
│       │   ├── scripts/
│       │   └── workflows/
│       ├── agents/
│       ├── assets/
│       │   ├── audio/
│       │   │   ├── bgm/
│       │   │   └── sfx/
│       │   │       ├── camera/
│       │   │       ├── counter/
│       │   │       ├── crowd/
│       │   │       ├── data/
│       │   │       ├── film/
│       │   │       ├── fluid/
│       │   │       ├── glass/
│       │   │       ├── impact/
│       │   │       ├── light/
│       │   │       ├── mech/
│       │   │       ├── paper/
│       │   │       ├── riser/
│       │   │       ├── scifi/
│       │   │       ├── text/
│       │   │       ├── transition/
│       │   │       └── ui/
│       │   ├── brand/
│       │   ├── lib/
│       │   │   └── helpers/
│       │   │       └── __tests__/
│       │   ├── readme/
│       │   │   ├── examples/
│       │   │   └── sponsors/
│       │   └── scripts/
│       ├── demos/
│       │   ├── _fixtures/
│       │   ├── _legacy/
│       │   │   ├── _fixtures/
│       │   │   ├── _textures/
│       │   │   ├── camera/
│       │   │   │   ├── depth-layer-moves/
│       │   │   │   └── tension-camera-moves/
│       │   │   ├── data/
│       │   │   │   ├── avatar-grid-radial-build-colorize/
│       │   │   │   ├── counter-confetti/
│       │   │   │   ├── cycle-glass-node-morph/
│       │   │   │   ├── hatch-depth/
│       │   │   │   ├── odometer-digit-roll/
│       │   │   │   ├── particle-celebrate-hits/
│       │   │   │   ├── particle-sand-fill/
│       │   │   │   └── ring-diagram-annotation-reveal/
│       │   │   ├── effects/
│       │   │   │   ├── dashboard-glow-highlight-pill/
│       │   │   │   ├── fui-hud-moves/
│       │   │   │   ├── icon-performance-moves/
│       │   │   │   ├── light-play-moves/
│       │   │   │   ├── line-boil/
│       │   │   │   └── riso-print-hits/
│       │   │   ├── interaction/
│       │   │   │   ├── ai-stream-response/
│       │   │   │   ├── chip-lift-to-user-pill/
│       │   │   │   ├── collab-cursor-moves/
│       │   │   │   ├── command-palette-summon/
│       │   │   │   └── input-trigger-moves/
│       │   │   ├── outro/
│       │   │   │   └── edit-hook-moves/
│       │   │   ├── rhythm/
│       │   │   │   ├── beat-cut-moves/
│       │   │   │   ├── montage-rhythm-moves/
│       │   │   │   ├── panel-grid-moves/
│       │   │   │   ├── rhythm-interrupt-moves/
│       │   │   │   ├── smear-multiples/
│       │   │   │   ├── spectrum-morph-ui/
│       │   │   │   ├── speed-ramp-freeze/
│       │   │   │   └── trailer-grammar-moves/
│       │   │   ├── transition/
│       │   │   │   ├── bubble-swarm-takeover/
│       │   │   │   ├── color-block-step-wipe/
│       │   │   │   ├── cube-navigation/
│       │   │   │   ├── page-turn-transitions/
│       │   │   │   ├── paper-plane-messenger/
│       │   │   │   ├── shot-transitions/
│       │   │   │   ├── transition-travel/
│       │   │   │   └── wipe-transitions/
│       │   │   ├── typography/
│       │   │   │   ├── cel-flash-stomp/
│       │   │   │   ├── scramble/
│       │   │   │   ├── split-flap-title/
│       │   │   │   ├── type-assembly-moves/
│       │   │   │   ├── type-entrance-moves/
│       │   │   │   ├── typewriter-moves/
│       │   │   │   └── typing-code-block/
│       │   │   └── ui-entrance/
│       │   │       ├── element-body-moves/
│       │   │       ├── floating-glossy-label-pills/
│       │   │       ├── morph-from-primitive/
│       │   │       ├── paper-craft-moves/
│       │   │       ├── platform-hinge-rise/
│       │   │       ├── runway-ground-skim/
│       │   │       ├── skeleton-reveal/
│       │   │       ├── svg-shape-morph/
│       │   │       └── wall-reveal-moves/
│       │   ├── _textures/
│       │   ├── camera/
│       │   │   ├── basic-3d-scene/
│       │   │   ├── crash-zoom-punch/
│       │   │   ├── cursor-flyover/
│       │   │   ├── depth-layer-moves/
│       │   │   ├── graze-face-tour/
│       │   │   ├── overhead-camera-moves/
│       │   │   ├── space-camera-moves/
│       │   │   ├── steep-tilt-glide/
│       │   │   ├── tension-camera-moves/
│       │   │   └── terminal-3d/
│       │   ├── data/
│       │   │   ├── before-after-slider-scrub/
│       │   │   ├── chart-live-moves/
│       │   │   ├── gauge-readout-moves/
│       │   │   ├── scroll-brake-moves/
│       │   │   └── timeline-travel/
│       │   ├── effects/
│       │   │   ├── assemble-then-type-flyin/
│       │   │   ├── aurora-bloom-bg-flip/
│       │   │   ├── brand-frame-snap/
│       │   │   ├── fui-hud-moves/
│       │   │   ├── glow-flyline-moves/
│       │   │   ├── icon-performance-moves/
│       │   │   ├── impact-feedback/
│       │   │   ├── light-play-moves/
│       │   │   ├── radial-ripple-phone-chips/
│       │   │   ├── riso-print-hits/
│       │   │   ├── scan-bracket-sweep/
│       │   │   ├── scanline-annotate-focus/
│       │   │   ├── scanline-assemble-flyin/
│       │   │   ├── slam-entrance-moves/
│       │   │   └── spotlight-sweep-moves/
│       │   ├── interaction/
│       │   │   ├── autolayout-gap-dial/
│       │   │   ├── canvas-materialize-moves/
│       │   │   ├── chip-grid-single-select-blackout/
│       │   │   ├── collab-cursor-moves/
│       │   │   ├── glass-pill-dictation-typing/
│       │   │   ├── hashtag-to-pill-materialize/
│       │   │   ├── picker-carousel-feature-cycle/
│       │   │   ├── segmented-thumb-hero/
│       │   │   ├── theme-switch-moves/
│       │   │   ├── type-and-filter/
│       │   │   └── voice-waveform-live/
│       │   ├── opening/
│       │   │   ├── crane-rise-reveal/
│       │   │   ├── dataviz-landscape-open/
│       │   │   ├── fracture/
│       │   │   ├── icon-field-colorize/
│       │   │   ├── letterspace-materialize/
│       │   │   ├── magician-card-flourish/
│       │   │   ├── orbit-ring-title-open/
│       │   │   ├── spotlight-hero-card/
│       │   │   ├── stroke-segment-build/
│       │   │   └── text-as-mask/
│       │   ├── outro/
│       │   │   ├── grain-dissolve/
│       │   │   ├── logo-shrink-wordmark-lockup/
│       │   │   ├── neon-triple-marquee/
│       │   │   ├── outro-group-photo-launch/
│       │   │   ├── ui-strip-away-outro/
│       │   │   └── ui-to-brand-morph/
│       │   ├── rhythm/
│       │   │   ├── beat-cut-moves/
│       │   │   ├── beat-step-list-theme-cycle/
│       │   │   ├── panel-grid-moves/
│       │   │   ├── quad-split-parallel-scenes/
│       │   │   ├── rhythm-interrupt-moves/
│       │   │   ├── sakuga-timing-shift/
│       │   │   ├── speed-ramp-freeze/
│       │   │   └── trailer-grammar-moves/
│       │   ├── transition/
│       │   │   ├── bottom-push-stack-wipe/
│       │   │   ├── card-flip-reveal/
│       │   │   ├── card-flock-tumble/
│       │   │   ├── circle-match-iris/
│       │   │   ├── gradient-transition/
│       │   │   ├── line-carry-transition/
│       │   │   ├── mosaic-reframe/
│       │   │   ├── page-turn-transitions/
│       │   │   ├── print-texture-transitions/
│       │   │   ├── shot-transitions/
│       │   │   ├── tear-streak-transitions/
│       │   │   ├── transition-hidden-cut/
│       │   │   ├── transition-travel/
│       │   │   ├── white-flash-logo-simplify-cut/
│       │   │   └── wipe-transitions/
│       │   ├── typography/
│       │   │   ├── blur-slide/
│       │   │   ├── brace-expand/
│       │   │   ├── brand-ink-open/
│       │   │   ├── countdown-arc-scatter/
│       │   │   ├── flying-words/
│       │   │   ├── glitch-cycle/
│       │   │   ├── gradient-word-sweep/
│       │   │   ├── lead-word-zoom-assemble/
│       │   │   ├── marker-underline-title/
│       │   │   ├── outline-word-fill/
│       │   │   ├── paper-title-card/
│       │   │   ├── pill-chip-slot-cycle-handled/
│       │   │   ├── pill-slot-cycle/
│       │   │   ├── text-column-converge/
│       │   │   ├── title-demote-to-label/
│       │   │   ├── type-assembly-moves/
│       │   │   ├── type-entrance-moves/
│       │   │   ├── type-rhythm-sync/
│       │   │   ├── typewriter-moves/
│       │   │   ├── vertical-word-roll-blur-cycle/
│       │   │   ├── word-relay-filmstrip/
│       │   │   └── word-relay-geometry/
│       │   └── ui-entrance/
│       │       ├── avatar-bracket-carousel/
│       │       ├── bezier-source-converge-merge/
│       │       ├── card-stack/
│       │       ├── carousel-3d/
│       │       ├── clipcard-looping/
│       │       ├── cloner-depth-echo/
│       │       ├── deck-deal-flyin/
│       │       ├── doc-park-left-pill-deal/
│       │       ├── document-typewriter-reveal/
│       │       ├── draw-svg-trace/
│       │       ├── element-body-moves/
│       │       ├── integration-hub-map/
│       │       ├── list-reveal/
│       │       ├── list-stack-press/
│       │       ├── neon-frame-forerun/
│       │       ├── neon-frame-orbit-drop/
│       │       ├── page-waterfall-wall/
│       │       ├── product-card-progressive-assemble/
│       │       ├── radial-wave/
│       │       ├── research-card-stack-scroll/
│       │       ├── row-embed/
│       │       ├── value-stagger-gradient/
│       │       └── wall-reveal-moves/
│       ├── gallery/
│       │   ├── api/
│       │   ├── media/
│       │   │   └── poster/
│       │   └── source/
│       ├── jianying-export/
│       ├── publish/
│       ├── references/
│       │   ├── sequences/
│       │   └── shots/
│       │       ├── camera/
│       │       ├── data/
│       │       ├── effects/
│       │       ├── interaction/
│       │       ├── opening/
│       │       ├── outro/
│       │       ├── rhythm/
│       │       ├── transition/
│       │       ├── typography/
│       │       └── ui-entrance/
│       ├── shot-polish/
│       │   ├── final-notes/
│       │   └── notes/
│       ├── template/
│       │   ├── public/
│       │   │   ├── audio/
│       │   │   └── textures/
│       │   │       └── live/
│       │   ├── scripts/
│       │   ├── src/
│       │   │   ├── aifl/
│       │   │   │   └── live/
│       │   │   └── themes/
│       │   └── themes/
│       ├── videos/
│       │   └── readme-workflow/
│       │       └── compositions/
│       │           └── components/
│       └── workbench/
│           ├── demosrc/
│           │   ├── _fixtures/
│           │   ├── _legacy/
│           │   │   ├── _fixtures/
│           │   │   ├── _textures/
│           │   │   ├── camera/
│           │   │   │   ├── depth-layer-moves/
│           │   │   │   └── tension-camera-moves/
│           │   │   ├── data/
│           │   │   │   ├── avatar-grid-radial-build-colorize/
│           │   │   │   ├── counter-confetti/
│           │   │   │   ├── cycle-glass-node-morph/
│           │   │   │   ├── hatch-depth/
│           │   │   │   ├── odometer-digit-roll/
│           │   │   │   ├── particle-celebrate-hits/
│           │   │   │   ├── particle-sand-fill/
│           │   │   │   └── ring-diagram-annotation-reveal/
│           │   │   ├── effects/
│           │   │   │   ├── dashboard-glow-highlight-pill/
│           │   │   │   ├── fui-hud-moves/
│           │   │   │   ├── icon-performance-moves/
│           │   │   │   ├── light-play-moves/
│           │   │   │   ├── line-boil/
│           │   │   │   └── riso-print-hits/
│           │   │   ├── interaction/
│           │   │   │   ├── ai-stream-response/
│           │   │   │   ├── chip-lift-to-user-pill/
│           │   │   │   ├── collab-cursor-moves/
│           │   │   │   ├── command-palette-summon/
│           │   │   │   └── input-trigger-moves/
│           │   │   ├── outro/
│           │   │   │   └── edit-hook-moves/
│           │   │   ├── rhythm/
│           │   │   │   ├── beat-cut-moves/
│           │   │   │   ├── montage-rhythm-moves/
│           │   │   │   ├── panel-grid-moves/
│           │   │   │   ├── rhythm-interrupt-moves/
│           │   │   │   ├── smear-multiples/
│           │   │   │   ├── spectrum-morph-ui/
│           │   │   │   ├── speed-ramp-freeze/
│           │   │   │   └── trailer-grammar-moves/
│           │   │   ├── transition/
│           │   │   │   ├── bubble-swarm-takeover/
│           │   │   │   ├── color-block-step-wipe/
│           │   │   │   ├── cube-navigation/
│           │   │   │   ├── page-turn-transitions/
│           │   │   │   ├── paper-plane-messenger/
│           │   │   │   ├── shot-transitions/
│           │   │   │   ├── transition-travel/
│           │   │   │   └── wipe-transitions/
│           │   │   ├── typography/
│           │   │   │   ├── cel-flash-stomp/
│           │   │   │   ├── scramble/
│           │   │   │   ├── split-flap-title/
│           │   │   │   ├── type-assembly-moves/
│           │   │   │   ├── type-entrance-moves/
│           │   │   │   ├── typewriter-moves/
│           │   │   │   └── typing-code-block/
│           │   │   └── ui-entrance/
│           │   │       ├── element-body-moves/
│           │   │       ├── floating-glossy-label-pills/
│           │   │       ├── morph-from-primitive/
│           │   │       ├── paper-craft-moves/
│           │   │       ├── platform-hinge-rise/
│           │   │       ├── runway-ground-skim/
│           │   │       ├── skeleton-reveal/
│           │   │       ├── svg-shape-morph/
│           │   │       └── wall-reveal-moves/
│           │   ├── _textures/
│           │   ├── camera/
│           │   │   ├── basic-3d-scene/
│           │   │   ├── crash-zoom-punch/
│           │   │   ├── cursor-flyover/
│           │   │   ├── depth-layer-moves/
│           │   │   ├── graze-face-tour/
│           │   │   ├── overhead-camera-moves/
│           │   │   ├── space-camera-moves/
│           │   │   ├── steep-tilt-glide/
│           │   │   ├── tension-camera-moves/
│           │   │   └── terminal-3d/
│           │   ├── data/
│           │   │   ├── before-after-slider-scrub/
│           │   │   ├── chart-live-moves/
│           │   │   ├── gauge-readout-moves/
│           │   │   ├── scroll-brake-moves/
│           │   │   └── timeline-travel/
│           │   ├── effects/
│           │   │   ├── assemble-then-type-flyin/
│           │   │   ├── aurora-bloom-bg-flip/
│           │   │   ├── brand-frame-snap/
│           │   │   ├── fui-hud-moves/
│           │   │   ├── glow-flyline-moves/
│           │   │   ├── icon-performance-moves/
│           │   │   ├── impact-feedback/
│           │   │   ├── light-play-moves/
│           │   │   ├── radial-ripple-phone-chips/
│           │   │   ├── riso-print-hits/
│           │   │   ├── scan-bracket-sweep/
│           │   │   ├── scanline-annotate-focus/
│           │   │   ├── scanline-assemble-flyin/
│           │   │   ├── slam-entrance-moves/
│           │   │   └── spotlight-sweep-moves/
│           │   ├── interaction/
│           │   │   ├── autolayout-gap-dial/
│           │   │   ├── canvas-materialize-moves/
│           │   │   ├── chip-grid-single-select-blackout/
│           │   │   ├── collab-cursor-moves/
│           │   │   ├── glass-pill-dictation-typing/
│           │   │   ├── hashtag-to-pill-materialize/
│           │   │   ├── picker-carousel-feature-cycle/
│           │   │   ├── segmented-thumb-hero/
│           │   │   ├── theme-switch-moves/
│           │   │   ├── type-and-filter/
│           │   │   └── voice-waveform-live/
│           │   ├── opening/
│           │   │   ├── crane-rise-reveal/
│           │   │   ├── dataviz-landscape-open/
│           │   │   ├── fracture/
│           │   │   ├── icon-field-colorize/
│           │   │   ├── letterspace-materialize/
│           │   │   ├── magician-card-flourish/
│           │   │   ├── orbit-ring-title-open/
│           │   │   ├── spotlight-hero-card/
│           │   │   ├── stroke-segment-build/
│           │   │   └── text-as-mask/
│           │   ├── outro/
│           │   │   ├── grain-dissolve/
│           │   │   ├── logo-shrink-wordmark-lockup/
│           │   │   ├── neon-triple-marquee/
│           │   │   ├── outro-group-photo-launch/
│           │   │   ├── ui-strip-away-outro/
│           │   │   └── ui-to-brand-morph/
│           │   ├── rhythm/
│           │   │   ├── beat-cut-moves/
│           │   │   ├── beat-step-list-theme-cycle/
│           │   │   ├── panel-grid-moves/
│           │   │   ├── quad-split-parallel-scenes/
│           │   │   ├── rhythm-interrupt-moves/
│           │   │   ├── sakuga-timing-shift/
│           │   │   ├── speed-ramp-freeze/
│           │   │   └── trailer-grammar-moves/
│           │   ├── transition/
│           │   │   ├── bottom-push-stack-wipe/
│           │   │   ├── card-flip-reveal/
│           │   │   ├── card-flock-tumble/
│           │   │   ├── circle-match-iris/
│           │   │   ├── gradient-transition/
│           │   │   ├── line-carry-transition/
│           │   │   ├── mosaic-reframe/
│           │   │   ├── page-turn-transitions/
│           │   │   ├── print-texture-transitions/
│           │   │   ├── shot-transitions/
│           │   │   ├── tear-streak-transitions/
│           │   │   ├── transition-hidden-cut/
│           │   │   ├── transition-travel/
│           │   │   ├── white-flash-logo-simplify-cut/
│           │   │   └── wipe-transitions/
│           │   ├── typography/
│           │   │   ├── blur-slide/
│           │   │   ├── brace-expand/
│           │   │   ├── brand-ink-open/
│           │   │   ├── countdown-arc-scatter/
│           │   │   ├── flying-words/
│           │   │   ├── glitch-cycle/
│           │   │   ├── gradient-word-sweep/
│           │   │   ├── lead-word-zoom-assemble/
│           │   │   ├── marker-underline-title/
│           │   │   ├── outline-word-fill/
│           │   │   ├── paper-title-card/
│           │   │   ├── pill-chip-slot-cycle-handled/
│           │   │   ├── pill-slot-cycle/
│           │   │   ├── text-column-converge/
│           │   │   ├── title-demote-to-label/
│           │   │   ├── type-assembly-moves/
│           │   │   ├── type-entrance-moves/
│           │   │   ├── type-rhythm-sync/
│           │   │   ├── typewriter-moves/
│           │   │   ├── vertical-word-roll-blur-cycle/
│           │   │   ├── word-relay-filmstrip/
│           │   │   └── word-relay-geometry/
│           │   └── ui-entrance/
│           │       ├── avatar-bracket-carousel/
│           │       ├── bezier-source-converge-merge/
│           │       ├── card-stack/
│           │       ├── carousel-3d/
│           │       ├── clipcard-looping/
│           │       ├── cloner-depth-echo/
│           │       ├── deck-deal-flyin/
│           │       ├── doc-park-left-pill-deal/
│           │       ├── document-typewriter-reveal/
│           │       ├── draw-svg-trace/
│           │       ├── element-body-moves/
│           │       ├── integration-hub-map/
│           │       ├── list-reveal/
│           │       ├── list-stack-press/
│           │       ├── neon-frame-forerun/
│           │       ├── neon-frame-orbit-drop/
│           │       ├── page-waterfall-wall/
│           │       ├── product-card-progressive-assemble/
│           │       ├── radial-wave/
│           │       ├── research-card-stack-scroll/
│           │       ├── row-embed/
│           │       ├── value-stagger-gradient/
│           │       └── wall-reveal-moves/
│           ├── docs/
│           ├── i18n/
│           │   └── ru/
│           ├── proj-stub/
│           ├── public/
│           ├── scripts/
│           └── src/
│               ├── cards/
│               │   └── inkpress/
│               ├── panels/
│               ├── preview/
│               ├── remotion/
│               └── timeline/
├── tests/
│   ├── assets/
│   ├── clis/
│   └── fixtures/
│       └── invalid/
│           ├── body-frontmatter/
│           ├── page--cro/
│           ├── unclosed-frontmatter/
│           └── versiontest/
└── tools/
    ├── aisa/
    │   └── evals/
    ├── clis/
    ├── composio/
    └── integrations/
```
