import Foundation
import Alamofire
import SwiftyJSON
import PerfectMarkdown
import SwiftSoup

struct Constants {
    static let readmeUrl = "https://raw.githubusercontent.com/vsouza/awesome-ios/master/README.md"
}

class AwesomeiOS {

	func generateHTML() -> String? {

		var data:String?

		Alamofire.request(Constants.readmeUrl).response { response in
			if let mdText = response.data {
				data = String(data: mdText, encoding: String.Encoding.utf8)!.markdownToHTML
			}
		}

		return data
	}

}
