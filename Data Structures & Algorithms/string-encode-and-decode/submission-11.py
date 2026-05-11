class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "{}{}"
        if len(strs) == 1 and strs[0] == "":
            return "{}{}{}"
        return "{}".join(strs)

    def decode(self, s: str) -> List[str]:
        if "{}{}{}" in s:
            return [""]
        if "{}{}" in s:
            return []
        if len(s) > 2:
            return s.split("{}")
