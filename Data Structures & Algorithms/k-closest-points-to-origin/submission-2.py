class Solution:
    def quickSort(self, points, dist_list, start, end):
        if end - start + 1 <= 1:
            return points

        pivot = dist_list[end]
        left = start # pointer for left side
        # partition: elements smaller than pivot moves to left
        for i in range(start, end):
            if dist_list[i][0] < pivot[0]:
                tmp = dist_list[left]
                dist_list[left] = dist_list[i]
                dist_list[i] = tmp
                left += 1
        
        dist_list[end] = dist_list[left]
        dist_list[left] = pivot

        self.quickSort(points, dist_list, start, left - 1)
        self.quickSort(points, dist_list, left + 1, end)

    def kClosest(self, points, k):
        dist_list = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            dist_list.append((dist, point))

        self.quickSort(points, dist_list, 0, len(points) - 1)

        k_points = []
        for point in dist_list:
            if k > 0:
                k_points.append(point[1])
                k -= 1
            else:
                break
          
        return k_points








