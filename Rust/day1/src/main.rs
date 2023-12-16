use std::fs::File;
use std::io::{self, BufRead};

fn main() -> Result<(), io::Error> {
    let file = File::open("src/input.txt")?;
    let reader = io::BufReader::new(file);
    let mut first_num: i32 = -1;
    let mut last_num: i32 = -1;
    let mut result: i32 = 0;

    for l in reader.lines() {
        let l = l?;

        for c in l.chars() {
            if c.is_digit(10) {
                let val = c.to_digit(10).unwrap() as i32;

                if first_num == -1 {
                    first_num = val;
                }
                last_num = val;
            }
        }
        result += first_num * 10 + last_num;
        first_num = -1;
    }

    println!("{}", result);

    Ok(())
}
