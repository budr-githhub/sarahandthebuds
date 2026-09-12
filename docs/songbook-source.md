# Songbook selections

## Current release — September 12, 2026

Bud approved publication. [PR #5](https://github.com/budr-githhub/sarahandthebuds/pull/5) merged as `b99f8f14fa54306b6f864a4cdce9365f35decd2f`; Cloudflare reported a successful production deployment. Fresh production responses verified the band-only hero and its image asset, full songbook with 146 cover/holiday entries, request-only originals, and corrected inline spacing. Earlier pending-release notes below are historical and superseded. Initial cached songbook requests returned 404 immediately after deployment; fresh requests succeeded.

Live pages: [Homepage](https://sarahandthebuds.com/) and [Songbook](https://sarahandthebuds.com/songbook).


Source: Sarah & the Buds Master Song List.docx, August 2026, supplied by Bud and retained outside git in Documents/Plan & Adapt - Source Files. Only artist/title metadata is published; no lyrics, chords or performance notes. Suggested future additions are excluded. Standard punctuation and title spelling normalized.

70 songs across 44 artists. Native details/summary controls collapse the entire songbook and expand multi-song artists; single-song entries remain directly readable once the songbook opens.

- The Band: It Makes No Difference; Up on Cripple Creek; The Weight
- The Beatles: Across the Universe; All You Need Is Love; Blackbird; Hey Jude; If I Fell; Let It Be; Till There Was You
- Bob Dylan: Blowin’ in the Wind; Don’t Think Twice, It’s All Right; Like a Rolling Stone; The Times They Are A-Changin’
- Boston: Peace of Mind
- boygenius: Not Strong Enough
- Chappell Roan: Pink Pony Club
- Coldplay: Yellow
- Counting Crows: A Long December; Accidentally in Love; Anna Begins
- The Cranberries: Zombie
- Crowded House: Don’t Dream It’s Over; Weather with You
- Dolly Parton: Jolene
- Ella Langley: Choosin' Texas
- Elle King & Tyler Childers: Jersey Giant
- First Aid Kit: Emmylou
- Fleetwood Mac: Landslide
- Glen Hansard & Markéta Irglová: Low Rising
- Gracie Abrams: That's So True
- Green Day: Basket Case; Boulevard of Broken Dreams; Give Me Novacaine
- Guns N' Roses / Sheryl Crow: Sweet Child o' Mine
- Jimmy Eat World: The Middle
- John Denver: Take Me Home, Country Roads
- Kacey Musgraves: The Architect; Biscuits
- Kaitlin Butts: Marfa Lights; You Ain’t Got to Die (to Be Dead to Me)
- Miranda Lambert: Armadillo; In His Arms
- Muscadine Bloodline: Goose Chase; Pieces
- Nancy Sinatra: These Boots Are Made for Walkin'
- Neil Diamond: Sweet Caroline
- Neil Young: Harvest Moon; Lotta Love
- Nelly Furtado: I'm Like a Bird
- Noah Kahan: Stick Season
- Oasis: Champagne Supernova
- Patsy Cline: Crazy
- Paul Simon: Graceland
- The Rolling Stones: Paint It Black
- Shania Twain: Whose Bed Have Your Boots Been Under?
- Sixpence None the Richer: Kiss Me; There She Goes
- Stealers Wheel: Stuck in the Middle with You
- TLC: No Scrubs
- Tom Petty: Free Fallin'; I Won't Back Down; Wildflowers
- Townes Van Zandt: Pancho and Lefty
- Tracy Chapman: Fast Car; Give Me One Reason
- U2: Every Breaking Wave; Song for Someone
- Van Morrison: Brown Eyed Girl
- Willie Nelson: Always on My Mind

## Complete reference

`src/data/songbook.json` is the current metadata inventory. The full `/songbook` reference transcribes every entry in the August table of contents before “Consider adding audience favorites,” deduplicating Song for Someone and Emmylou. Counts: 137 covers, 41 originals, 5 holiday, 1 specialty = 184. Holiday includes the source entry A Very Willie Christmas. Full reference uses titles without inferred artist attribution. Source spellings are lightly normalized for known cover titles; no lyrics or chords are published. Homepage retains 70 selected songs in compact rows inside a single disclosure.

## Artist examples and owner additions — 2026-09-12

Bud requested exactly one homepage row per artist: roughly two examples, with a third for short titles and natural wrapping. Added owner-supplied With or Without You, One and Acrobat (U2); Into the Mystic (Van Morrison); Falling Slowly and Song of Good Hope (Glen Hansard & Markéta Irglová). Newly requested examples are prioritized. The full reference now contains 189 unique entries (Into the Mystic was already present); these additions are authorized by Bud beyond the August document. A second full-list link follows the collapsible section. Supersedes earlier row/count notes; release pending in PR #5.

## Original songs by request — 2026-09-12

Bud requested removal of the specialty section and no named originals yet. Both public pages now say “Original songs available by request” with a contact link. Removed original/specialty arrays from public songbook metadata and removed Merry Mary from the holiday listing and homepage copy. The source document remains unchanged. The reference displays 146 covers/seasonal entries (142 covers, four holiday selections), plus the request-only originals section. This supersedes earlier public counts and original-title lists. PR #5 remains pending release.
