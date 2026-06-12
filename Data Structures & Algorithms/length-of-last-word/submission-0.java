class Solution {
    public int lengthOfLastWord(String s) {
        String[] arryString=s.trim().split("\\s+");
        return arryString[arryString.length-1].length();
    }
}