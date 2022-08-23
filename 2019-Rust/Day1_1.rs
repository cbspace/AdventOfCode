use std::{fs::File,path::Path};
use std::io::{BufRead, BufReader};

fn main() {
    let path = Path::new("./input.txt");
    let file = File::open(&path).unwrap();

    let mut fuel_vector: Vec<i32> = Vec::new();
    let mut fuel_total = 0;

    let reader = BufReader::new(file);
    for line in reader.lines() {
        let current: i32 = line.unwrap().parse().unwrap();
        fuel_vector.push(current)
    }

    for n in fuel_vector {
        let f = n / 3 - 2;
        fuel_total += f;
    }

    println!("{}",fuel_total);
}
