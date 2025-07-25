class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int[] arr = new int[m + n];

        int i = 0;
        int j = 0;
        int k = 0;

        while (i < m && j < n) {
            if (nums1[i] < nums2[j]) {
                arr[k] = nums1[i];
                i++;
            } else {
                arr[k] = nums2[j];
                j++;
            }
            k++;
        }

        while (i < m) {
            arr[k] = nums1[i];
            i++;
            k++;
        }

        while (j < n) {
            arr[k] = nums2[j];
            j++;
            k++;
        }

        if (arr.length % 2 == 0) {
            return (arr[(arr.length / 2) - 1] + arr[arr.length / 2]) / 2.0;
        }
        return arr[arr.length / 2];
    }
}