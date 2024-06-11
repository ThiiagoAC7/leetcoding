use std::collections::HashMap;

pub fn run() {
    // let nums = [15,11,7,2];
    // let target = 9;

    let nums = [3,2,4];
    let target = 6;

    // let nums = [3,3];
    // let target = 6;

    let result  = two_sum(nums.to_vec(), target);
    println!("{:?}", result);
}


fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut result: [i32; 2] = [0; 2];

    let mut map: HashMap<i32, i32> = HashMap::new();

    let mut value;

    for (idx, &num) in nums.iter().enumerate() {
        value = target - num;
        println!("{},{}, {}", idx, value, num);

        if map.contains_key(&num) {
            result[0] = idx as i32;
            result[1] = *map.get(&num).unwrap();
            return result.to_vec();
        }

        map.insert(value, idx as i32);
    }


    return result.to_vec();
}
