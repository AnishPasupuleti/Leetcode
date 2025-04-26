# 🧠 Problem Explanation

Given an array of integers `nums` and a target value `target`, return the indices of the two numbers such that they add up to `target`.

**Example:**
Input: nums = [2,7,11,15], target = 9  
Output: [0,1] 

---

# ⚙️ Approach

- Use a hash map to track elements.
- For each number, compute the required complement.
- If complement is in the map, return the pair of indices.

---

# ⏱️ Time & Space Complexity

- **Time:** O(n)
- **Space:** O(n)
