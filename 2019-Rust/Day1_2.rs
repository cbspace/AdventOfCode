use std::{fs::File,path::Path};
use std::io::{BufRead, BufReader};

fn main() {
    let path = Path::new("./input.txt");
    let file = File::open(&path).unwrap();

    let mut fuel_vector: Vec<i32> = Vec::new();
    let mut fuel_total: i64 = 0;

    let reader = BufReader::new(file);
    for line in reader.lines() {
        let current: i32 = line.unwrap().parse().unwrap();
        fuel_vector.push(current)
    }
    
    for n in fuel_vector {
        let mut f = n;
        loop {
            f = f / 3 - 2;
            if f <= 0 {break;}
            fuel_total += f as i64;
        }
    }

    println!("{}",fuel_total);
}
