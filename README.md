### pyregex - regular expression basics

##Be specific
When the patterns we define are very specific, the engine can help us perform quick
integrity checks before the actual pattern matching is executed.
For instance, if we pass the expression /\w{15}/ to the engine to match it against the text hello, the engine could decide to check whether the input string is actually at least 15 characters long instead of matching the expression.

## Don't be greedy
We've studied about quantifiers in Chapter 1, Introducing Regular Expressions, and we learned the difference between greedy and reluctant quantifiers. We also found that the quantifiers are greedy by default.
What does this mean in terms of performance? It means that the engine will always
try to catch as many characters as possible, and then reduce the scope step-by-step until the matching is done. This could potentially make the regular expression slow if the match is typically short. Keep in mind, however, that this is only applicable if the match is usually short.
