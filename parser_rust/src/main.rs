extern crate serde_json;

use serde_json::{Value};

fn main() {
    let v: Value = serde_json::from_reader(std::io::stdin()).unwrap();
    println!("{}", v);
}
