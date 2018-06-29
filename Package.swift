// swift-tools-version:4.1.0
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "awesome-ios",
    dependencies: [
				.package(url: "https://github.com/Alamofire/Alamofire.git", from: "4.0.0"),
				.package(url: "https://github.com/PerfectlySoft/Perfect-Markdown.git", from: "3.0.0"),
				.package(url: "https://github.com/scinfu/SwiftSoup.git", from: "1.7.1")
    ],
    targets: [
        .target(
            name: "awesome-ios",
            dependencies: ["Alamofire", "PerfectMarkdown", "SwiftSoup"]),
    ]
)
