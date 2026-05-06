class Solution {

    Map<String, List<String>> map = new HashMap<>();

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String str: strs) {
            sb.append(str);
        }
        String answer = sb.toString();
        map.put(answer, strs);
        return answer;
    }

    public List<String> decode(String str) {
        return map.get(str);
    }
}
