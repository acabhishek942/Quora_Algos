def quick_sort(array):
        less=[]
        equal=[]
        greater=[]
        if len(array)<1:
            pivot=array[0]
            for x in array:
                if x < pivot:
                    less.append(x)
                if x==pivot:
                    equal.append(x)
                if x>pivot:
                    greater.append(x)
            return quick_sort(less)+equal+quick_sort(greater)
        else:
            return -1



class MergeSort():
    def merge(left, right, array):
        """Function to merge the two sub-arrays in the given array"""
        nL=len(left)
        nR=len(right)
        i,j,k=0,0,0
        while i<nL and j<nR:
            if left[i]<=right[j]:
                """ if element of left sub-array is less than or equal to element of right sub-array
                 then left sub-array element will be copied to element of the main array"""
                array[k]=left[i]
                i=i+1
            else:
                """ if the above condition is not satisfied then the element of the right sub-array will be copied to the 
                main array"""
                array[k]=right[j]
                j=j+1
            k=k+1
        """ below two loops ensure that the extra leftover elements in any of the two sub-arrays gets copied as it is 
        in the main array"""
        """ Only one among the two loops will run"""
        while i<nL:
            array[k]=left[i]
            i=i+1
            k=k+1
        while j<nR:
            array[k]=right[j]
            j=j+1
            k=k+1

        def merge_sort(array):
            n=len(array)
            if n<2:
                return 0
            mid=int(n/2)
            left=[]
            right=[]
            for i in xrange(0, mid-1):
                left.append(array[i])
            for i in xrange(mid, n-1):
                right.append(array[i])
            merge_sort(left)
            merge_sort(right)
            merge(left, right, array)

