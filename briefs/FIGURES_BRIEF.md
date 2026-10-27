# Figures brief: Permit Path illustrations

Permit Path books need road signs and teaching diagrams. You draw them as original SVG files, by hand-written SVG code, and place them in the core chapters. Read `docs/decisions.md` and `briefs/CORE_SPEC.md` first. The model is `layout/fig/signs_regulatory_core.svg`: match its style exactly.

## Rules
- **Original work only.** Draw from the FHWA MUTCD 11th edition specifications (shapes, colors, legends, layouts are a public federal standard). Never copy, trace or download an image from any book, website or clip art set. Never look at other DMV books.
- **Real MUTCD colors** (the ebook shows them in color; print turns them into grays): red #C8102E, yellow #FFCD00, fluorescent yellow-green #C6D52B, orange #F47920, green #006B3F, blue #003F87, brown #6B4423, white #fff, black #1c1c1c, fluorescent pink #E8418C. Road gray #d9d9d9, lane paint white with a thin #888 outline so it shows on white paper, yellow paint #FFCD00 with a #888 outline.
- **B&W must still read.** Never rely on color alone. Every sign gets a label and a sub-label naming the shape and color ("Yellow diamond"). Diagrams use labels and arrows, not color coding.
- **Text in figures:** `font-family="Inter, Arial, sans-serif"`; labels 11px weight 600, sub-labels 9.5px weight 500 #555, legends inside signs bold. Minimum 9px. No em or en dashes, no years, no brand names, no state names.
- **Size:** viewBox width 460, height 200 to 360 (prints 4.6 in wide on a 6 x 9 page; keep it under about 3.5 in tall). Panels hold 3 to 8 items in a grid.
- **State-neutral.** No figure that varies by state (no fines, no state speed or distance values). National MUTCD facts are fine (for example the 15-foot railroad stop line minimum).
- **Diagrams:** top-down view, cars as rounded rectangles with a darker windshield band so direction is clear, your car labeled "You", arrows for paths (#1c1c1c, 2.5px, arrowhead marker), numbered steps in black circles with white numbers when showing a sequence.
- File names: lowercase, digits and underscores only, `layout/fig/NAME.svg`.

## Placing figures
In the chapter Markdown, on its own line where the topic is taught: `![Caption sentence.](fig/NAME.svg)`. Captions are one plain sentence that tells the reader what to notice, and name colors in words. At most 1 figure per about 400 words; never two figures back to back without text between them. Do not change chapter text except to add a short lead-in sentence where needed. Do not touch `{{INSERT:...}}` lines, quizzes or bank files.

## Checking your work
1. `python3 tools/render_fig.py NAME1 NAME2 ... /tmp/claude-0/-home-claude/9d4de182-a7b0-5f49-bd9e-983574378387/scratchpad/figs_<yourtag>` renders the grayscale print preview. Open every PNG with the Read tool and look at it. Fix overlaps, clipped text, unreadable gray-on-gray, wrong shapes.
2. Check every sign against the MUTCD (shape, colors, legend wording, arrow directions) and every diagram against the chapter text and its quiz/bank questions: a figure must never contradict the text.
3. `python3 tools/originality_check.py check core/chNN.md` still passes.
4. Write `core/notes/figures_<yourtag>.md`: each figure, what it shows, its MUTCD section or source, and where you placed it.

Reply with the list of figures, where each was placed, and anything you were unsure was accurate. No em or en dashes in files or reply.
