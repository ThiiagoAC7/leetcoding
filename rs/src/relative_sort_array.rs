// https://leetcode.com/problems/relative-sort-array/
use std::collections::HashMap;

pub fn run() {
    //let arr1 = Vec::from([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]);
    //let arr2 = Vec::from([2, 1, 4, 3, 9, 6]);

    let arr1 = Vec::from([2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]);
    let arr2 = Vec::from([2,42,38,0,43,21]);

    let result = relative_sort_array(arr1, arr2);
    let expected = Vec::from([2,42,38,0,43,21,5,7,12,12,13,23,24,24,27,29,30,31,33,48]);

    assert_eq!(result, expected);

    println!("{:?}", result);
}

fn relative_sort_array(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {
    let mut result = Vec::new();

    let mut map: HashMap<i32, i32> = HashMap::new();


    for arr1_value in arr1 {
        *map.entry(arr1_value).or_insert(0) += 1;       
    }
    
    for arr2_value in arr2 {
        if let Some(count) = map.get(&arr2_value) {
            for _ in 0..*count {
                result.push(arr2_value);
            }
            
            map.remove(&arr2_value);
        }
    }

    let mut rest = Vec::new();

    for (key, value) in map {
        for _ in 0..value {
            rest.push(key);
        }
    }

    rest.sort();
    result.extend(rest);

    return result;
}
