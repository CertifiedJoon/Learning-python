Space Usage favors Rabin-Karp 
One major advantage of Rabin-Karp is that it uses O(1) auxiliary storage space, which is great if the pattern string you're looking for is very large. For example, if you're looking for all occurrences of a string of length 107 in a longer string of length 109, not having to allocate a table of 107 machine words for a failure function or shift table is a major win. Both Boyer-Moore and KMP use Ω(n) memory on a pattern string of length n, so Rabin-Karp would be a clear win here.

Worst-Case Single-Match Efficiency Favors Boyer-Moore or KMP
Rabin-Karp suffers from two potential worst cases. First, if the particular prime numbers used by Rabin-Karp are known to a malicious adversary, that adversary could potentially craft an input that causes the rolling hash to match the hash of a pattern string at each point in time, causing the algorithm's performance to degrade to Ω((m - n + 1)n) on a string of length m and pattern of length n. If you're taking untrusted strings as input, this could potentially be an issue. Neither Boyer-Moore nor KMP have these weaknesses.

Worst-Case Multiple-Match Efficiency favors KMP.
Similarly, Rabin-Karp is slow in the case where you want to find all matches of a pattern string in the case where that pattern appears a large number of times. For example, if you're looking for a string of 105 copies of the letter a in text string consisting of 109copies of the letter a with Rabin-Karp, then there will be lots of spots where the pattern string appears, and each will require a linear scan. This can also lead to a runtime of Ω((m + n - 1)n).

Many Boyer-Moore implementations suffer from this second rule, but will not have bad runtimes in the first case. And KMP has no pathological worst-cases like these.

Best-Case Performance favors Boyer-Moore
One advantage of the Boyer-Moore algorithm is that it doesn't necessarily have to scan all the characters of the input string. Specifically, the Bad Character Rule can be used to skip over huge regions of the input string in the event of a mismatch. More specifically, the best-case runtime for Boyer-Moore is O(m / n), which is much faster than what Rabin-Karp or KMP can provide.

Generalizations to Multiple Strings favor KMP
Suppose you have a fixed set of multiple text strings that you want to search for, rather than just one. You could, if you wanted to, run multiple passes of Rabin-Karp, KMP, or Boyer-Moore across the strings to find all the matches. However, the runtime of this approach isn't great, as it scales linearly with the number of strings to search for. On the other hand, KMP generalizes nicely to the Aho-Corasick string-matching algorithm, which runs in time O(m + n + z), where z is the number of matches found and n is the combined length of the pattern strings. Notice that there's no dependence here on the number of different pattern strings being searched for!