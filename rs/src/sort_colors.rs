// https://leetcode.com/problems/sort-colors

pub fn run() {
    
    let mut nums = Vec::from([2,0,2,1,1,0]);
    println!("{:?}", nums);
    sort_colors(&mut nums);
    println!("{:?}", nums);

}

// Order -> red : 0, 1 : white, 2 : blue
fn sort_colors(nums: &mut Vec<i32>) {

    let low : i32 = 0;
    let high : i32 = nums.len() as i32 - 1;
    
    quicksort(nums, low, high);
}

fn quicksort(nums: &mut Vec<i32>, low : i32, high: i32){
    if low < high {
        let p = partition(nums, low, high);

        quicksort(nums, low, p - 1);
        quicksort(nums, p + 1, high);
    }
}

fn partition(nums: &mut Vec<i32>, low : i32, high: i32) -> i32 {
    let p = nums[high as usize];
    
    let mut i = low - 1;

    for j in low .. high {
        if nums[j as usize] <= p {
            i += 1;
            nums.swap(i as usize, j as usize);
        }
    }

    nums.swap(i as usize + 1, high as usize);
    return i + 1;
}
