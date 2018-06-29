import Foundation
import Alamofire
import SwiftyJSON
import PerfectMarkdown
import SwiftSoup

Alamofire.request("https://raw.githubusercontent.com/vsouza/awesome-ios/master/README.md").response { response in
	if let mdText = response.data {
		var backToString = String(data: mdText, encoding: String.Encoding.utf8) as String!
		if let html = backToString!.markdownToHTML {
do {
		let els: Elements = try SwiftSoup.parse(html).select("a")
    for link: Element in els.array() {
        let linkHref: String = try link.attr("href")
				print(linkHref)
        let linkText: String = try link.text()
    }

} catch Exception.Error(let type, let message) {
    print(message)
} catch {
    print("error")
}
		}
	}
}

RunLoop.main.run()

