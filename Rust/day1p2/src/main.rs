use regex::Regex;
use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};

fn main() -> Result<(), io::Error> {
    let special_strs = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4",
        "5", "6", "7", "8", "9",
    ];

    let mut str_to_number = HashMap::new();

    for (i, &special_str) in special_strs.iter().enumerate() {
        let val = ((i as i32) % 9) + 1;
        str_to_number.insert(special_str, val);
    }

    let first_exp = format!("({})", special_strs.join("|"));
    let first_re = Regex::new(&exp).unwrap();

    let file = File::open("src/input.txt")?;
    let reader = io::BufReader::new(file);
    let mut result = 0;

    for line_result in reader.lines() {
        let first = first_re.find(&line_result.unwrap());
        //.filter_map(|x| str_to_number.get(x.as_str()).copied())
        //.collect();
    }

    println!("{}", result);

    Ok(())
}
