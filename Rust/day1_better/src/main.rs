use std::fs;

fn main() -> Result<(), std::io::Error> {
    let input = fs::read_to_string("src/input.txt")?;
    let mut result = 0;

    for line in input.lines() {
        let numbers: Vec<i32> = line
            .chars()
            .filter_map(|c| c.to_digit(10).map(|d| d as i32))
            .collect();

        if let Some(&first) = numbers.first() {
            if let Some(&last) = numbers.last() {
                result += first * 10 + last;
            }
        }
    }

    println!("{}", result);

    Ok(())
}
