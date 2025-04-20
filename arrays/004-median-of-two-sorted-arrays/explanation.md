# 🧠 Problem Explanation

Given two sorted arrays, merge them and find the median of the combined array.

---

# ⚙️ Approach

- Combine `nums1` and `nums2` into a single list.
- Sort the merged list.
- If the list has an even number of elements:
  - Return the average of the two middle values.
- If the list has an odd number of elements:
  - Return the middle value.

---

# 🔢 Example

nums1 = [1, 2], nums2 = [3, 4]  
→ Merged = [1, 2, 3, 4]  
→ Median = (2 + 3) / 2 = 2.5

---

# ⏱️ Time & Space Complexity

- **Time:** O((m+n) log(m+n)) — due to sorting
- **Space:** O(m+n) — merged list
