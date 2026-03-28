# 2.2.A. Overview of methodology

+----------------+----------------+----------------+----------------+
| Labeling Mode  | What It    | Color          | Visual Effect  |
|                | Checks     |                |                |
+----------------+----------------+----------------+----------------+
| Ownership  | **Who wrote    |  White | **Rainbow.**   |
|            | this?** Shows  |                | Single colors  |
|                | if a file is   |                | are            |
|                | owned by one   |                | individuals;   |
|                | person (Solo)  |                | bright White   |
|                | or everyone    |                | is a team      |
|                | (Collective).  |                | effort.        |
+----------------+----------------+----------------+----------------+
| Cognitive  | **How hard is  |            | **Purple.**    |
| Load       | it to read?**  |            | The deeper the |
|                | Highlights     | Purple | purple, the    |
|                | confusing      |                | harder the     |
|                | logic that     |                | logic is to    |
|                | requires high  |                | follow.        |
|                | mental effort. |                |                |
+----------------+----------------+----------------+----------------+
| Churn  | **How often    | Orange | **Orange.**    |
|            | does it        |                | Bright orange  |
|                | change?**      |                | indicates a    |
|                | Identifies     |                | file that      |
|                | files that are |                | refuses to     |
|                | constantly     |                | settle down.   |
|                | being          |                |                |
|                | rewritten or   |                |                |
|                | patched.       |                |                |
+----------------+----------------+----------------+----------------+
| Safety     | **Is it        | Red    | **Red to       |
|            | bulletproof?** |                | Cyan.** Red is |
|                | Checks for     | to     | fragile/risky; |
|                | defensive code |                | Cyan is        |
|                | (error         |  Cyan  | f              |
|                | handling) vs.  |                | ortified/safe. |
|                | risky code.    |                |                |
+----------------+----------------+----------------+----------------+
| Tech       | **Are there    | Red    | **Red.**       |
| Debt       | shortcuts?**   |                | Glowing red    |
|                | Scans for      |                | highlights     |
|                | \"TODOs\",     |                | unfinished     |
|                | \"Hacks\", and |                | business.      |
|                | temporary      |                |                |
|                | fixes.         |                |                |
+----------------+----------------+----------------+----------------+
| Doc        | **Is it        | Library    | **Gold.**      |
| Mode       | explained?**   | Gold       | Bright gold    |
|                | Measures the   |                | indicates      |
|                | quality of     |                | library-grade  |
|                | instruction    |                | documentation. |
|                | manuals and    |                |                |
|                | comments.      |                |                |
+----------------+----------------+----------------+----------------+
| Commit     | **Is it        | Green          | **Green.**     |
| Heat       | fresh?** Shows |                | Radioactive    |
|                | where work is  |                | green means it |
|                | happening      |                | was edited     |
|                | *right now*    |                | today.         |
|                | vs. months     |                |                |
|                | ago.           |                |                |
+----------------+----------------+----------------+----------------+
| Test       | **Is it        | Pink           | **Pink.**      |
| Coverage   | verified?**    |                | Glowing pink   |
|                | Checks if the  |                | means the code |
|                | code has a     |                | is heavily     |
|                | safety net of  |                | tested.        |
|                | tests proving  |                |                |
|                | it works.      |                |                |
+----------------+----------------+----------------+----------------+
| []{#a          | **Tabs or      | Green Vs.      | **Green vs     |
| nchor-63}Civil | Spaces?**      | Yellow         | Yellow.** Blue |
| War            | Checks for     |                | indicates a    |
|                | indentation    |                | messy mix of   |
|                | consistency.   |                | both.          |
+----------------+----------------+----------------+----------------+
| []{#ancho      | **Is there     | Purple         | **Purple.** A  |
| r-64}Graveyard | dead code?**   |                | \"haunted\"    |
|                | Finds blocks   |                | purple glow    |
|                | of code that   |                | indicates      |
|                | were commented |                | historical     |
|                | out and        |                | hoarding.      |
|                | abandoned.     |                |                |
+----------------+----------------+----------------+----------------+
| API Exposure   | **Is it        | #ff007f        | **Electric     |
|                | public?**      |                | Rose.**        |
|                | Highlights the | Electric Rose  | Indicates a    |
|                | entry points   |                | public         |
|                | where the      |                | interface or   |
|                | system talks   |                | endpoint.      |
|                | to the outside |                |                |
|                | world.         |                |                |
+----------------+----------------+----------------+----------------+
| Concurrency    | **Is it        | #7b2ff7        | **             |
| Exposure       | m              |                | Ultraviolet.** |
|                | ultitasking?** | Electric       | Indicates      |
|                | Highlights     | Ultraviolet    | potential race |
|                | complex        |                | conditions or  |
|                | timing,        |                | timing risks.  |
|                | threads, or    |                |                |
|                | asynchronous   |                |                |
|                | logic.         |                |                |
+----------------+----------------+----------------+----------------+
| State Flux     | **Is the data  | #ffb84e        | **Clyde        |
| Exposure       | changing?**    |                | Orange.**      |
|                | Highlights     | Clyde Orange   | Indicates      |
|                | variables that |                | \"boiling\"    |
|                | are constantly |                | data that is   |
|                | being          |                | hard to track. |
|                | mod            |                |                |
|                | ified/mutated. |                |                |
+----------------+----------------+----------------+----------------+


