import XCTest
@testable import AwesomeiOS
import Foundation
import SwiftSoup

class AwesomeiOSTests: XCTestCase {

	static var allTests : [(String, (AwesomeiOSTests) -> () throws -> Void)] {
    return [
      ("testDuplicates", testDuplicates),
      ("testLinks", testLinks)
    ]
  }

  func testDuplicates() {
  	let aws = AwesomeiOS()
  	let html = aws.generateHTML()
  	if let htmlStr = html {
			do {
				let els: Elements = try SwiftSoup.parse(htmlStr).select("a")
    		for link: Element in els.array() {
        		let linkHref: String = try link.attr("href")
        		let linkText: String = try link.text()
    		}
			} catch Exception.Error(let type, let message) {
					print(type)
    			print(message)
			} catch {
    			print("error")
			}

  	}
  	XCTAssertTrue(true)
  }

  func testLinks() {
  	XCTAssertTrue(true)
  }
}
