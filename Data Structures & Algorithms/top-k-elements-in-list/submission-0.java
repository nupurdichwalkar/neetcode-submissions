class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int num: nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        PriorityQueue<Integer> queue = new PriorityQueue<>((a,b) -> map.get(a) - map.get(b));

        for(int key: map.keySet()) {
            queue.add(key);
            if(queue.size() > k) {
               queue.poll();
            } 
        }

        int[] result = new int[k];
        for(int i=0; i<k; i++) {
            result[i] = queue.poll();
        }
        return result;
    }
}
