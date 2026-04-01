class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        if strs == [""]:
            return " "
        sngl_str = "~".join(strs)
        return sngl_str
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s == " ":
            return [""]
        dcd = s.split("~")
        return dcd