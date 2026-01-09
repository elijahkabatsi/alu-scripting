# Regular Expressions - ALU Scripting

This folder contains all tasks for the **Regular Expressions** project in the ALU Scripting curriculum. Each script demonstrates usage of Ruby regular expressions with Oniguruma, as required by the exercises.

## Structure

| File | Description |
|------|-------------|
| `0-simply_match_school.rb` | Matches the word `School` in a string. |
| `1-repetition_token_0.rb` | Uses the `*` repetition token to match `hbt*n`. |
| `2-repetition_token_1.rb` | Uses the `+` repetition token to match `hbt+n`. |
| `3-repetition_token_2.rb` | Uses the `?` optional repetition token to match `hbt?n`. |
| `4-repetition_token_3.rb` | Uses `{min,max}` repetition token to match `hbt{1,3}n`. |
| `5-beginning_and_end.rb` | Matches strings starting with `h`, ending with `n`, with exactly one character in between (`h.n`). |
| `6-phone_number.rb` | Matches **exactly 10-digit phone numbers** (`^\d{10}$`). |
| `7-OMG_WHY_ARE_YOU_SHOUTING.rb` | Matches **only capital letters** in a string (`[A-Z]`). |
| `8-textme.rb` | Extracts **sender, receiver, and flags** from TextMe SMS logs using `[from:(.*?)]`, `[to:(.*?)]`, `[flags:(.*?)]`. |
| `9-passed_linkedin_regex_challenge.jpg` | Screenshot of LinkedIn regex puzzle completion (“Congratulations” screen). |

## Usage

All Ruby scripts are executable and take **one argument**. Example:

./0-simply_match_school.rb "Best School"
