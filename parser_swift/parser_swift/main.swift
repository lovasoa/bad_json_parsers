// Thris program reads nested JSON arrays on its standard input
// It exits with EXIT_FAILURE when it fails to decode its input as nested JSON array

import Foundation

struct NestedArrays : Decodable {
    var depth: Int

    init(from decoder: Decoder) throws {
        let container = try decoder.singleValueContainer()
        let children = try container.decode([NestedArrays].self)
        self.depth = 1 + (children.first?.depth ?? 0)
    }
}

do{
    let input = FileHandle.standardInput.readDataToEndOfFile()
    let nested = try JSONDecoder().decode(NestedArrays.self, from: input)
    print("Nested arrays with depth \(nested.depth)")
} catch let parsingError {
    print(parsingError)
    exit(EXIT_FAILURE)
}
