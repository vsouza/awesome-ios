<img src="https://raw.githubusercontent.com/vsouza/awesome-ios/master/awesome_logo.png">

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Join the chat at https://gitter.im/norio-nomura/SwiftTalkInJapanese](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/vsouza/awesome-ios?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/vsouza/awesome-ios.svg?branch=master)](https://travis-ci.org/vsouza/awesome-ios)

A curated list of awesome iOS frameworks, libraries, tutorials, Xcode plugins, components and much more.
The list is divided into categories such as Frameworks, Components, Testing and others, open source projects, free and paid services. There is no pre-established order of items in each category, the order is for contribution. If you want to contribute, please read the [guide](https://github.com/vsouza/awesome-ios/blob/master/CONTRIBUTING.md).

Projects in Swift will be marked with :large_orange_diamond:, Swift Extensions will be marked with 🔶[e] and ⌚ for Apple Watch projects. Feel free to add your project.

### Content

- [Getting Started](#getting-started)
- [Library and Frameworks](#libraries-and-frameworks)
    - [Animation](#animation)
    - [Apple TV](#apple-tv)
    - [Authentication](#authentication)
    - [Bridging](#bridging)
    - [Cache](#cache)
    - [Color](#color)
    - [Command Line](#command-line)
    - [Core Data](#core-data)
    - [Charts](#charts)
    - [Database](#database)
    - [Date & Time](#date--time)
    - [Graphics](#graphics)
    - [Hardware](#hardware)
        - [Bluetooth](#bluetooth)
        - [Camera](#camera)
        - [Location](#location)
        - [iBeacon](#ibeacon)
        - [Other Hardware](#other-hardware)
    - [EventBus](#eventbus)
    - [Files](#files)
    - [Functional Programming](#functional-programming)
    - [JSON](#json)
    - [Layout](#layout)
    - [Localization](#localization)
    - [Logging](#logging)
    - [Maps](#maps)
    - [Media](#media)
        - [Audio](#audio)
        - [Image](#image)
        - [GIF](#gif)
        - [PDF](#pdf)
        - [Video](#video)
    - [Messaging](#messaging)
    - [Machine Learning](#machine-learning)
    - [Networking](#networking)
    - [Push Notifications](#push-notifications)
        - [Push Notification Providers](#push-notification-providers)
    - [Passbook](#passbook)
    - [Permissions](#permissions)
    - [Regex](#regex)
    - [Security](#security)
    - [Text](#text)
    - [Walkthrough / Intro / Tutorial](#walkthrough--intro--tutorial)
    - [URL Scheme](#url-scheme)
    - [UI](#ui)
        - [Activity Indicator](#activity-indicator)
        - [Alert View](#alerts)
        - [Calendar](#calendar)
        - [Form](#form)
        - [Table View](#table-view)
        - [TextField & TextView](#textfield--textview)
        - [Keyboard](#keyboard)
        - [Button](#button)
        - [Menu](#menu)
        - [Label](#label)
        - [Popup](#popup)
        - [Pull to Refresh](#pull-to-refresh)
        - [Slider](#slider)
        - [Tab Bar](#tab-bar)
    - [Websocket](#websocket)
    - [Code Quality](#code-quality)
    - [Analytics](#analytics)
    - [Payments](#payments)
    - [Products](#products)
    - [Utility](#utility)
- [Server](#server)
- [Project setup](#project-setup)
- [Dependency / Package Manager](#dependency--package-manager)
- [Testing](#testing)
    - [TDD / BDD](#tdd--bdd)
    - [A/B Testing](#ab-testing)
    - [UI Testing](#ui-testing)
    - [Beta Distribution](#beta-distribution)
    - [Other Testing](#other-testing)
- [Tools](#tools)
- [Rapid Development](#rapid-development)
  - [Injection](#injection)
- [Deployment](#deployment)
- [App Store](#app-store)
- [SDK](#sdk)
    - [Official](#official)
    - [Unofficial](#unofficial)
- [Xcode](#xcode)
    - [Plugins](#plugins)
    - [Themes](#themes)
    - [Other Xcode](#other-xcode)
- [Style Guides](#style-guides)
- [Good Websites](#good-websites)
    - [News, Blogs and more](#news-blogs-and-more)
    - [UIKit references](#uikit-references)
    - [Forums and discuss lists](#forums-and-discuss-lists)
    - [Tutorials and Keynotes](#tutorials-and-keynotes)
    - [Prototyping](#prototyping)
    - [Newsletters](#newsletters)
    - [Medium](#medium)
- [Twitter](#twitter)
- [Facebook Groups](#facebook-groups)
- [Podcasts](#podcasts)
- [Books](#books)
- [Other Awesome Lists](#other-awesome-lists)
- [Contributing](#contributing)

***
# Getting Started
 * [Start Developing with iOS](https://developer.apple.com/library/ios/referencelibrary/GettingStarted/DevelopiOSAppsSwift/) - Apple Guide. :large_orange_diamond:
 * [Lifehacker](http://lifehacker.com/i-want-to-write-ios-apps-where-do-i-start-1644802175) - I Want to Write iOS Apps. Where Do I Start?
 * [Codeproject](http://www.codeproject.com/Articles/88929/Getting-Started-with-iPhone-and-iOS-Development) - Getting Started with iPhone and iOS Development.
 * [Ray Wenderlich](https://www.raywenderlich.com/38557/learn-to-code-ios-apps-1-welcome-to-programming) - Learn to code iOS Apps.
 * [Stanford - Developing Apps to iOS](https://itunes.apple.com/us/itunes-u/developing-apps-for-ios-hd/id395605774?mt=10) - Stanford's iTunes U App Development Course (Audio and Video).
 * [Stanford - Developing iOS 8 Apps with Swift](https://itunes.apple.com/us/course/developing-ios-8-apps-swift/id961180099) - Stanford's 2015 iTunes U App Development Course. :large_orange_diamond:
 * [Programming with Objective-C by Apple](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html)
 * [Object-Oriented Programming with Objective-C by Apple](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/OOP_ObjC/Introduction/Introduction.html)
 * [Udacity: Beginning iOS App Development Nanodegree](https://www.udacity.com/course/beginning-ios-app-development-nanodegree--nd006) - Udacity's intro course on writing iOS apps [Paid Resource] :large_orange_diamond:
 * [Udacity: iOS Developer Nanodegree](https://www.udacity.com/course/ios-developer-nanodegree--nd003) - Udacity's full course on iOS developing [Paid Resource] :large_orange_diamond:


# Libraries And Frameworks

### Animation
 * [Pop](https://github.com/facebook/pop) - An extensible iOS and OS X animation library, useful for physics-based interactions.
 * [AnimationEngine](https://github.com/intuit/AnimationEngine) - Easily build advanced custom animations on iOS.
 * [Awesome-iOS-Animation](https://github.com/jackyzh/awesome-ios-animation) - Collection of Animation projects
 * [RZTransitions](https://github.com/Raizlabs/RZTransitions) - A library of custom iOS View Controller Animations and Interactions.
 * [DCAnimationKit](https://github.com/daltoniam/DCAnimationKit) - A collection of animations for iOS. Simple, just add water animations.
 * [Spring](https://github.com/MengTo/Spring) - A library to simplify iOS animations in Swift.
 * [Canvas](https://github.com/CanvasPod/Canvas) - Animate in Xcode without code http://canvaspod.io
 * [Fluent](https://github.com/matthewcheok/Fluent) - Swift animation made easy :large_orange_diamond:
 * [Cheetah](https://github.com/suguru/Cheetah) - Easy animation library on iOS with Swift2. :large_orange_diamond:
 * [RadialLayer](https://github.com/soheil/RadialLayer) - Animation for clickable elements (similar to Youtube Music). :large_orange_diamond:
 * [Pop By Example](https://github.com/hossamghareeb/Facebook-POP-Tutorial) - A project tutorial in how to use Pop animation framework by example.
 * [AppAnimations](http://www.appanimations.com) - Collection of iOS animations to inspire your next project
 * [EasyAnimation](https://github.com/icanzilb/EasyAnimation) - A Swift library to take the power of UIView.animateWithDuration() to a whole new level - layers, springs, chain-able animations, and mixing view/layer animations together. :large_orange_diamond:
 * [Animo](https://github.com/eure/Animo) - SpriteKit-like animation builders for CALayers. :large_orange_diamond:
 * [CurryFire](https://github.com/devinross/curry-fire) - A framework for creating unique animations.
 * [IBAnimatable](https://github.com/JakeLin/IBAnimatable) - Design and prototype UI, interaction, navigation, transition and animation for App Store ready Apps in Interface Builder with IBAnimatable. :large_orange_diamond:
 * [CKWaveCollectionViewTransition](https://github.com/CezaryKopacz/CKWaveCollectionViewTransition) - Cool wave like transition between two or more UICollectionView :large_orange_diamond:
 * [DaisyChain](https://github.com/alikaragoz/DaisyChain) - :link: Easy animation chaining :large_orange_diamond:
 * [SYBlinkAnimationKit](https://github.com/shoheiyokoyama/SYBlinkAnimationKit) - A blink effect animation framework for iOS, written in Swift. :large_orange_diamond:
 * [PulsingHalo](https://github.com/shu223/PulsingHalo) - iOS Component for creating a pulsing animation.
 * [DKChainableAnimationKit](https://github.com/Draveness/DKChainableAnimationKit) - :star: Chainable animations in Swift :large_orange_diamond:[e]
 * [JDAnimationKit](https://github.com/JellyDevelopment/JDAnimationKit) - Animate easy and with less code with Swift :large_orange_diamond:
 * [Advance](https://github.com/storehouse/Advance) - A powerful animation framework for iOS. :large_orange_diamond:
 * [UIView-Shake](https://github.com/andreamazz/UIView-Shake) - UIView category that adds shake animation
 * [Walker](https://github.com/RamonGilabert/Walker) - A new animation engine for your app. :large_orange_diamond:
 * [Morgan](https://github.com/RamonGilabert/Morgan) - An animation set for your app. :large_orange_diamond:
 * [MagicMove](https://github.com/patrickreynolds/MagicMove) - Keynote-style Magic Move transition animations :large_orange_diamond:

### Apple TV
 * [Voucher](https://github.com/rsattar/Voucher) - A simple library to make authenticating tvOS apps easy via their iOS counterparts.
 * [XCDYouTubeKit](https://github.com/0xced/XCDYouTubeKit) - YouTube video player for iOS, tvOS and OS X
 * [TVMLKitchen](https://github.com/toshi0383/TVMLKitchen) - Swifty TVML template manager without client-server :large_orange_diamond:
 * [BrowserTV](https://github.com/zats/BrowserTV) - Turn your TV into a dashboard displaying any webpage! :large_orange_diamond:
 * [Swift-GA-Tracker-for-Apple-tvOS](https://github.com/analytics-pros/Swift-GA-Tracker-for-Apple-tvOS) - Google Analytics tracker for Apple tvOS provides an easy integration of Google Analytics’ measurement protocol for Apple TV. :large_orange_diamond:

 ### Authentication
 * [Heimdallr.swift](https://github.com/rheinfabrik/Heimdallr.swift) - Easy to use OAuth 2 library for iOS, written in Swift. :large_orange_diamond:
 * [OhMyAuth](https://github.com/hyperoslo/OhMyAuth) - Simple OAuth2 library with a support of multiple services. :large_orange_diamond:
 * [AuthenticationViewController](https://github.com/raulriera/AuthenticationViewController) - A simple to use, standard interface for authenticating to oauth 2.0 protected endpoints via SFSafariViewController. :large_orange_diamond:
 * [OAuth2](https://github.com/p2/OAuth2) - OAuth2 framework for OS X and iOS, written in Swift. :large_orange_diamond:
 * [OAuthSwift](https://github.com/OAuthSwift/OAuthSwift) - Swift based OAuth library for iOS :large_orange_diamond:
 * [SimpleAuth](https://github.com/calebd/SimpleAuth) - Simple social authentication for iOS
 * [AlamofireOauth2](https://github.com/evermeer/AlamofireOauth2) - A swift implementation of OAuth2 :large_orange_diamond:

### Bridging
 * [RubyMotion](http://www.rubymotion.com/) - RubyMotion is a revolutionary toolchain that lets you quickly develop and test native iOS and OS X applications for iPhone, iPad and Mac, all using the Ruby language.
 * [JSPatch](https://github.com/bang590/JSPatch) - JSPatch bridge Objective-C and Javascript using the Objective-C runtime. You can call any Objective-C class and method in JavaScript by just including a small engine. JSPatch is generally use for hotfix iOS App.

### Cache
 * [Awesome Cache](https://github.com/aschuch/AwesomeCache) - Delightful on-disk cache :large_orange_diamond:
 * [mattress](https://github.com/buzzfeed/mattress) - iOS Offline Caching for Web Content :large_orange_diamond:
 * [Carlos](https://github.com/WeltN24/Carlos) - A simple but flexible cache :large_orange_diamond:
 * [HanekeSwift](https://github.com/Haneke/HanekeSwift) - A lightweight generic cache for iOS written in Swift with extra love for images. :large_orange_diamond:
 * [YYCache](https://github.com/ibireme/YYCache) - High performance cache framework for iOS.
 * [Cache](https://github.com/hyperoslo/Cache) - Nothing but Cache. :large_orange_diamond:

### Color
* [Chameleon](https://github.com/ViccAlexander/Chameleon) - A lightweight, yet powerful, flat color framework for iOS (ObjC & Swift). :large_orange_diamond:
* [SDevFlatColors](https://github.com/0x73/SDevFlatColors) - Flat Colors on Swift :large_orange_diamond:
* [ColorArt](https://github.com/vinhnx/ColorArt) - extract dominant colors from image like iTunes 11.
* [DynamicColor](https://github.com/yannickl/DynamicColor) - Yet another extension to manipulate colors easily in Swift. :large_orange_diamond:[e]
* [SwiftHEXColors](https://github.com/thii/SwiftHEXColors) - HEX color handling as an extension for UIColor. :large_orange_diamond:[e]
* [Colours](https://github.com/bennyguitar/Colours) - A beautiful set of predefined colors and a set of color methods to make your iOS/OSX development life easier.
* [UIColor-Hex-Swift](https://github.com/yeahdongcn/UIColor-Hex-Swift) - Convenience method for creating autoreleased color using RGBA hex string. :large_orange_diamond:
* [Crayons](https://github.com/Sephiroth87/Crayons) - An Xcode plugin to improve dealing with colors in your project
* [Hue](https://github.com/hyperoslo/Hue) - Hue is the all-in-one coloring utility that you'll ever need.
* [FlatUIColors](https://github.com/brynbellomy/FlatUIColors) - Flat UI color palette helpers written in Swift. :large_orange_diamond:
* [RandomColorSwift](https://github.com/onevcat/RandomColorSwift) - An attractive color generator for Swift. Ported from randomColor.js. :large_orange_diamond:
* [PFColorHash](https://github.com/PerfectFreeze/PFColorHash) - Generate color based on the given string. :large_orange_diamond:
* [ViralSwitch](https://github.com/andreamazz/ViralSwitch) - A UISwitch that infects its superview with its tint color.

### Command Line
* [Swiftline](https://github.com/Swiftline/Swiftline) - Swiftline is a set of tools to help you create command line applications. :large_orange_diamond:
* [CommandLine](https://github.com/jatoben/CommandLine) - A pure Swift library for creating command-line interfaces :large_orange_diamond:
* [Colors](https://github.com/paulot/Colors) - Terminal Colors for Swift :large_orange_diamond:
* [Commander](https://github.com/kylef/Commander) - Compose beautiful command line interfaces in Swift :large_orange_diamond:

### Charts
 * [ios-charts](https://github.com/danielgindi/ios-charts) - A powerful chart / graph framework, the iOS equivalent to [MPAndroidChart](https://github.com/PhilJay/MPAndroidChart). :large_orange_diamond:
 * [JTChartView](https://github.com/kubatru/JTChartView) - JTChartView is the new lightweight and fully customizable solution to draw a chart.
 * [PNChart](https://github.com/kevinzhow/PNChart) - A simple and beautiful chart lib used in Piner and CoinsMan for iOS
 * [BEMSimpleLineGraph](https://github.com/Boris-Em/BEMSimpleLineGraph) - Elegant Line Graphs for iOS (charting library).
 * [JBChartView](https://github.com/Jawbone/JBChartView) - iOS-based charting library for both line and bar graphs.
 * [iOSPlot](https://github.com/honcheng/iOSPlot) - Chart library for iOS.
 * [XYPieChart](https://github.com/xyfeng/XYPieChart) - A simple and animated Pie Chart for your iOS app.
 * [TEAChart](https://github.com/xhacker/TEAChart) - Simple and intuitive iOS chart library. Contribution graph, clock chart, and bar chart.
 * [EChart](https://github.com/zhuhuihuihui/EChart) - iOS/iPhone/iPad Chart, Graph. Event handling and animation supported.
 * [FSLineChart](https://github.com/ArthurGuibert/FSLineChart) - A line chart library for iOS.
 * [chartee](https://github.com/zhiyu/chartee) - a charting library for mobile platforms.
 * [ANDLineChartView](https://github.com/anaglik/ANDLineChartView) - ANDLineChartView is easy to use view-based class for displaying animated line chart.
 * [TWRCharts](https://github.com/chasseurmic/TWRCharts) - An iOS wrapper for ChartJS. Easily build animated charts by leveraging the power of native Obj-C code.
 * [SwiftCharts](https://github.com/i-schuetz/SwiftCharts) - Easy to use and highly customizable charts library for iOS. :large_orange_diamond:

### Core Data
 * [CWCoreData](https://github.com/jayway/CWCoreData) - Additions and utilities to make it concurrency easier with the Core Data framework.
 * [ObjectiveRecord](https://github.com/supermarin/ObjectiveRecord) - ActiveRecord for Objective-C.
 * [SSDataKit](https://github.com/soffes/SSDataKit) - Eliminate your Core Data boilerplate code.
 * [ios-queryable](https://github.com/martydill/ios-queryable) - ios-queryable is an implementation of IQueryable/IEnumerable for Core Data.
 * [ReactiveCoreData](https://github.com/apparentsoft/ReactiveCoreData) - ReactiveCoreData (RCD) is an attempt to bring Core Data into the ReactiveCocoa (RAC) world.
 * [Ensembles](https://github.com/drewmccormack/ensembles) - A synchronization framework for Core Data.
 * [SLRESTfulCoreData](https://github.com/OliverLetterer/SLRESTfulCoreData) - Objc naming conventions, autogenerated accessors at runtime, URL substitutions and intelligent attribute mapping.
 * [Mogenerator](https://github.com/rentzsch/mogenerator) - Automatic Core Data code generation.
 * [HardCoreData](https://github.com/Krivoblotsky/HardCoreData) - CoreData stack and controller that will never block UI thread.
 * [encrypted-core-data](https://github.com/project-imas/encrypted-core-data) - Core Data encrypted SQLite store using SQLCipher.
 * [MagicalRecord](https://github.com/magicalpanda/MagicalRecord) - Super Awesome Easy Fetching for Core Data.
 * [QueryKit](https://github.com/QueryKit/QueryKit) - A simple type-safe Core Data query language. :large_orange_diamond:
 * [CoreStore](https://github.com/JohnEstropia/CoreStore) - Powerful Core Data framework for Incremental Migrations, Fetching, Observering, etc. :large_orange_diamond:
 * [Core Data Query Interface](https://github.com/prosumma/CoreDataQueryInterface) A type-safe, fluent query framework for Core Data. :large_orange_diamond:
 * [Graph](https://github.com/CosmicMind/Graph) - An elegant data-driven framework for CoreData in Swift. :large_orange_diamond:
 * [CoreDataDandy](https://github.com/fuzz-productions/CoreDataDandy) - A feature-light wrapper around Core Data that simplifies common database operations. :large_orange_diamond:
 * [Sync](https://github.com/hyperoslo/Sync) - Modern JSON synchronization to Core Data :large_orange_diamond:
 * [AlecrimCoreData](https://github.com/Alecrim/AlecrimCoreData) - A powerful and simple Core Data wrapper framework written in Swift. :large_orange_diamond:

### Database
 * [Realm](https://github.com/realm/realm-cocoa) - The alternative to CoreData and SQLite: Simple, modern and fast.
 * [YapDatabase](https://github.com/yapstudios/YapDatabase) - YapDatabase is an extensible database for iOS & Mac.
 * [Couchbase Mobile](http://developer.couchbase.com/mobile/) - Couchbase document store for mobile with cloud sync.
 * [FMDB](https://github.com/ccgus/fmdb) - A Cocoa / Objective-C wrapper around SQLite.
 * [Akaibu-NSUserDefaults](https://github.com/roytang121/Akaibu-NSUserDefaults) - a Swifty Key-value store for archiving NSObject in only one line of code. Class properties are automatically mapped and archived under the hood.
 * [FCModel](https://github.com/marcoarment/FCModel) - An alternative to Core Data for people who like having direct SQL access.
 * [Zephyr](https://github.com/ArtSabintsev/Zephyr) - Effortlessly sync NSUserDefaults over iCloud :large_orange_diamond:
 * [Prephirences](https://github.com/phimage/Prephirences) - Prephirences is a Swift library that provides useful protocols and convenience methods to manage application preferences, configurations and app-state. :large_orange_diamond:
 * [Storez](https://github.com/SwiftKitz/Storez) - Safe, statically-typed, store-agnostic key-value storage (with namespace support). :large_orange_diamond:
 * [SwiftyUserDefaults](https://github.com/radex/SwiftyUserDefaults) - Statically-typed NSUserDefaults. :large_orange_diamond:
 * [swiftydb](https://github.com/Oyvindkg/swiftydb) - Making SQLite databases a blast :large_orange_diamond:
 * [SugarRecord](https://github.com/pepibumur/SugarRecord) - Data persistence management library written in Swift 2.0 :large_orange_diamond:
 * [SQLite.swift](https://github.com/stephencelis/SQLite.swift) - A type-safe, Swift-language layer over SQLite3. :large_orange_diamond:
 * [GRDB.swift](https://github.com/groue/GRDB.swift) - A versatile SQLite toolkit for Swift :large_orange_diamond:
 * [SwiftData](https://github.com/ryanfowler/SwiftData) - Simple and Effective SQLite Handling in Swift :large_orange_diamond:
 * [Fluent](https://github.com/qutheory/fluent) - Simple ActiveRecord implementation for working with your database in Swift. :large_orange_diamond:
 * [RealmIncrementalStore](https://github.com/eure/RealmIncrementalStore) - Realm-powered Core Data persistent store. :large_orange_diamond:

### Date & Time

* [Every.swift](https://github.com/samhann/Every.swift) - Wrapper for NSTimer :large_orange_diamond:
* [Timepiece](https://github.com/naoty/Timepiece) - Intuitive NSDate extensions :large_orange_diamond:[e]
* [SwiftDate](https://github.com/malcommac/SwiftDate) - Easy NSDate Management in Swift 2.0 :large_orange_diamond:
* [SwiftMoment](https://github.com/akosma/SwiftMoment) - A time and calendar manipulation library written in Swift 2 :large_orange_diamond:
* [DateTools](https://github.com/MatthewYork/DateTools) - Dates and times made easy in Objective-C
* [Punctual.swift](https://github.com/harlanhaskins/Punctual.swift) - Swift dates, more fun. :large_orange_diamond:
* [SwiftyTimer](https://github.com/radex/SwiftyTimer) - Swifty API for NSTimer :large_orange_diamond:[e]
* [AFDateHelper](https://github.com/melvitax/AFDateHelper) - Convenience extension for NSDate in Swift :large_orange_diamond:[e]
* [Tempo](https://github.com/remirobert/Tempo) - Date and time manager for iOS/OSX written in Swift :large_orange_diamond:

### Graphics
* [Graphicz](https://github.com/SwiftKitz/Graphicz) - Light-weight, operator-overloading-free complements to CoreGraphics! :large_orange_diamond:
* [PKCoreTechniques](https://github.com/pkluz/PKCoreTechniques) - The code for my CoreGraphics+CoreAnimation talk, held during the 2012 iOS Game Design Seminar at the Technical University Munich.
* [MPWDrawingContext](https://github.com/mpw/MPWDrawingContext) - An Objective-C wrapper for CoreGraphics CGContext
* [DePict](https://github.com/davidcairns/DePict) - A simple, declarative, functional drawing framework, in Swift! :large_orange_diamond:
* [SwiftSVG](https://github.com/mchoe/SwiftSVG) -  A single pass SVG parser with multiple interface options (String, NS/UIBezierPath, CAShapeLayer, and NS/UIView). :large_orange_diamond:

### Encryption
* [AESCrypt-ObjC](https://github.com/Gurpartap/AESCrypt-ObjC) - A simple and opinionated AES encrypt / decrypt Objective-C class that just works.
* [IDZSwiftCommonCrypto](https://github.com/iosdevzone/IDZSwiftCommonCrypto) - A wrapper for Apple's Common Crypto library written in Swift. :large_orange_diamond:

### Hardware

##### Bluetooth
 * [Discovery](https://github.com/omergul123/Discovery) - A very simple library to discover and retrieve data from nearby devices (even if the peer app works at background).
 * [LGBluetooth](https://github.com/l0gg3r/LGBluetooth) - Simple, block-based, lightweight library over CoreBluetooth. Will clean up your Core Bluetooth related code.
 * [PeerKit](https://github.com/jpsim/PeerKit) An open-source Swift framework for building event-driven, zero-config Multipeer Connectivity apps. :large_orange_diamond:
 * [simple-share](https://github.com/lauraskelton/simple-share) - Easy Proximity-based Bluetooth LE Sharing for iOS.
 * [BluetoothKit](https://github.com/rasmusth/BluetoothKit) - Easily communicate between iOS/OSX devices using BLE. :large_orange_diamond:
 * [CocoaMultipeer](https://github.com/manavgabhawala/CocoaMultipeer) - This repository is a peer to peer framework for OS X, iOS and watchOS 2 that presents a similar interface to the MultipeerConnectivity framework (which is iOS only) that lets you connect any 2 devices from any platform. :large_orange_diamond:
 * [Bluetonium](https://github.com/e-sites/Bluetonium) - Bluetooth mapping in Swift :large_orange_diamond:
 * [BlueCap](https://github.com/troystribling/BlueCap) - iOS Bluetooth LE framework :large_orange_diamond:

##### Camera
 * [TGCameraViewController](https://github.com/tdginternet/TGCameraViewController) - Custom camera with AVFoundation. Beautiful, light and easy to integrate with iOS projects.
 * [PBJVision](https://github.com/piemonte/PBJVision) - iOS camera engine, features touch-to-record video, slow motion video, and photo capture.
 * [Cool-iOS-Camera](https://github.com/GabrielAlva/Cool-iOS-Camera) - A fully customisable and modern camera implementation for iOS made with AVFoundation.
 * [SCRecorder](https://github.com/rFlex/SCRecorder) - Camera engine with Vine-like tap to record, animatable filters, slow motion, segments editing.
 * [ALCameraViewController](https://github.com/AlexLittlejohn/ALCameraViewController) - A camera view controller with custom image picker and image cropping. Written in Swift. :large_orange_diamond:
 * [ImagePicker](https://github.com/hyperoslo/ImagePicker) - Reinventing the way ImagePicker works. :large_orange_diamond:
 * [CameraManager](https://github.com/imaginary-cloud/CameraManager) - Simple Swift class to provide all the configurations you need to create custom camera view in your app. :large_orange_diamond:
 * [RxMediaPicker](https://github.com/RxSwiftCommunity/RxMediaPicker) - A reactive wrapper built around UIImagePickerController. :large_orange_diamond:
 * [RSBarcodes_Swift](https://github.com/yeahdongcn/RSBarcodes_Swift) - 1D and 2D barcodes reader and generators for iOS 8 with delightful controls. Now Swift. :large_orange_diamond:
 * [LLSimpleCamera](https://github.com/omergul123/LLSimpleCamera) - A simple, customizable camera control - video recorder for iOS.

##### Location
 * [IngeoSDK](https://github.com/IngeoSDK/ingeo-ios-sdk) - Always-On Location monitoring framework for iOS.
 * [LocationManager](https://github.com/intuit/LocationManager) - Provides a block-based asynchronous API to request the current location, either once or continuously.
 * [LocationKit](https://locationkit.io) - Advanced location SDK - highly accurate location data with very low battery drain and contextual location information
 * [SwiftLocation](https://github.com/malcommac/SwiftLocation) - CoreLocation Made Easy, 100% Swift :large_orange_diamond:
 * [SOMotionDetector](https://github.com/SocialObjects-Software/SOMotionDetector) - Simple library to detect motion. Based on location updates and acceleration.
 
##### iBeacon
 * [Proxitee](https://github.com/Proxitee/iOS-SDK) - Allows developers to create proximity aware applications utilizing iBeacons & geo fences.
 * [OWUProximityManager](https://github.com/ohwutup/OWUProximityManager) - iBeacons + CoreBluetooth.
 * [Vicinity](https://github.com/Instrument/Vicinity) - Vicinity replicates iBeacons (by analyzing RSSI) and supports broadcasting and detecting low-energy bluetooth devices in the background.
 * [BeaconEmitter](https://github.com/lgaches/BeaconEmitter) - Turn your Mac as an iBeacon.
 * [MOCA Proximity](https://mocaplatform.com/features) - Paid proximity marketing platform that lets you add amazing proximity  experiences to your app.

##### Other Hardware
 * [MotionKit](https://github.com/MHaroonBaig/MotionKit) - Get the data from Accelerometer, Gyroscope and Magnetometer in only Two or a few lines of code. CoreMotion now made insanely simple.
 * [DarkLightning](https://github.com/jensmeder/DarkLightning) -Simply the fastest way to transmit data between iOS and OSX

### EventBus
 * [Caravel](https://github.com/coshx/caravel) - A Swift event bus for UIWebView and JS :large_orange_diamond:
 * [SwiftEventBus](https://github.com/cesarferreira/SwiftEventBus) - A publish/subscribe event bus optimized for iOS8. :large_orange_diamond:
 * [PromiseKit](https://github.com/mxcl/PromiseKit) - Promises for iOS and OS X.
 * [Bolts](https://github.com/BoltsFramework/Bolts-ObjC) - Bolts is a collection of low-level libraries designed to make developing mobile apps easier, including tasks (promises) and app links (deep links).
 * [SwiftTask](https://github.com/ReactKit/SwiftTask) - Promise + progress + pause + cancel + retry for Swift.  :large_orange_diamond:
 * [When](https://github.com/vadymmarkov/When) - A lightweight implementation of Promises in Swift. :large_orange_diamond:

### Files
* [FileKit](https://github.com/nvzqz/FileKit) - Simple and expressive file management in Swift. :large_orange_diamond:
* [Zip](https://github.com/marmelroy/Zip) - Swift framework for zipping and unzipping files. :large_orange_diamond:
* [FileBrowser](https://github.com/marmelroy/FileBrowser) - Powerful Swift file browser for iOS. :large_orange_diamond:

### Functional Programming
* [Forbind](https://github.com/ulrikdamm/Forbind) - Functional chaining and promises in Swift. :large_orange_diamond:
* [Funky](https://github.com/brynbellomy/Funky) - Functional programming tools and experiments in Swift. :large_orange_diamond:
* [LlamaKit](https://github.com/LlamaKit/LlamaKit) - Collection of must-have functional Swift tools. :large_orange_diamond:
* [Oriole](https://github.com/tptee/Oriole) - A functional utility belt implemented as Swift 2.0 protocol extensions. :large_orange_diamond:[e]
* [Prelude](https://github.com/robrix/Prelude) - Swift µframework of simple functional programming tools. :large_orange_diamond:
* [Swiftx](https://github.com/typelift/Swiftx) - Functional data types and functions for any project. :large_orange_diamond:
* [Swiftz](https://github.com/typelift/Swiftz) -  Functional programming in Swift. :large_orange_diamond:
* [OptionalExtensions](https://github.com/RuiAAPeres/OptionalExtensions) - Swift µframework with extensions for the Optional Type. :large_orange_diamond:[e]
* [Hookah](https://github.com/HookahSwift/Hookah) - Hookah is a functional library for Swift. It's inspired by LoDash, Underscore project. :large_orange_diamond:
* [Argo](https://github.com/thoughtbot/Argo) - Functional JSON parsing library for Swift :large_orange_diamond:

### JSON
 * [JSONKit](https://github.com/johnezang/JSONKit) - Objective-C JSON.
 * [TouchJSON](https://github.com/TouchCode/TouchJSON) - A humane JSON Objective-C un-framework.
 * [JSON-Framework](https://github.com/stig/json-framework) -  This framework implements a strict JSON parser and generator in Objective-C.
 * [Mantle](https://github.com/Mantle/Mantle) - Model framework for Cocoa and Cocoa Touch.
 * [Groot](https://github.com/gonzalezreal/Groot) - Convert JSON dictionaries and arrays to and from Core Data managed objects.
 * [KZPropertyMapper](https://github.com/krzysztofzablocki/KZPropertyMapper) - Data mapping and validation with minimal amount of code.
 * [JSONModel](https://github.com/icanzilb/JSONModel) - Magical Data Modelling Framework for JSON. Create rapidly powerful, atomic and smart data model classes.
 * [SwiftyJSON](https://github.com/SwiftyJSON/SwiftyJSON) - The better way to deal with JSON data in Swift. :large_orange_diamond:
 * [FastEasyMapping](https://github.com/Yalantis/FastEasyMapping) - Serialize & deserialize JSON fast.
 * [OCMapper](https://github.com/aryaxt/OCMapper) - Objective-C & Swift library to easily map NSDictionary to model objects. :large_orange_diamond:
 * [ObjectMapper](https://github.com/Hearst-DD/ObjectMapper) - A framework written in Swift that makes it easy for you to convert your Model objects (Classes and Structs) to and from JSON. :large_orange_diamond:
 * [JASON](https://github.com/delba/JASON) - JSON parsing with outstanding performances and convenient operators. :large_orange_diamond:
 * [Gloss](https://github.com/hkellaway/Gloss) - A shiny JSON parsing library in Swift. :large_orange_diamond:
 * [Cereal](https://github.com/Weebly/Cereal) - Swift object serialization :large_orange_diamond:
 * [SwiftyJSONAccelerator](https://github.com/insanoid/SwiftyJSONAccelerator) - Generate Swift model files from JSON using either SwiftyJSON or ObjectMapper. Supports NSCoding and provides method for JSON string representation of the model. :large_orange_diamond:
 * [JSONCodable](https://github.com/matthewcheok/JSONCodable) - Hassle-free JSON encoding and decoding in Swift :large_orange_diamond:
 * [Coolie](https://github.com/nixzhu/Coolie) - Coolie helps you to create models (& their constructors) from JSON file. :large_orange_diamond:
 * [Tailor](https://github.com/zenangst/Tailor) - A super fast & convenient object mapper tailored for your needs. :large_orange_diamond:
 * [alexander](https://github.com/hodinkee/alexander) - An extremely simple JSON helper written in Swift. :large_orange_diamond:
 * [Freddy](https://github.com/bignerdranch/Freddy) - A reusable framework for parsing JSON in Swift. :large_orange_diamond:
 * [EVReflection](https://github.com/evermeer/EVReflection) - Reflection based JSON encoding and decoding. Including support for NSDictionary, NSCoding, Printable, Hashable and Equatable :large_orange_diamond:
 * [mapper](https://github.com/lyft/mapper) - Another JSON deserialization library for Swift :large_orange_diamond:
 * [AlamofireJsonToObjects](https://github.com/evermeer/AlamofireJsonToObjects) - An Alamofire extension which converts JSON response data into swift objects using EVReflection :large_orange_diamond:
 * [Jay](https://github.com/czechboy0/Jay) - Pure-Swift JSON parser & formatter. Linux & OS X ready. :large_orange_diamond:
 * [YYModel](https://github.com/ibireme/YYModel) - High performance model framework for iOS/OSX.

### Layout
* [FlexboxLayout](https://github.com/alexdrone/FlexboxLayout) - Port of Facebook's css-layout to Swift :large_orange_diamond:
* [Masonry](https://github.com/SnapKit/Masonry) - Harness the power of AutoLayout NSLayoutConstraints with a simplified, chainable and expressive syntax.
* [FLKAutoLayout](https://github.com/floriankugler/FLKAutoLayout) - UIView category which makes it easy to create layout constraints in code.
* [Façade](https://github.com/mamaral/Facade) - Programmatic view layout for the rest of us - an autolayout alternative.
* [PureLayout](https://github.com/PureLayout/PureLayout) - The ultimate API for iOS & OS X Auto Layout — impressively simple, immensely powerful. Objective-C and Swift compatible.
* [SnapKit](https://github.com/SnapKit/SnapKit) - A Swift Autolayout DSL for iOS & OS X. :large_orange_diamond:
* [Cartography](https://github.com/robb/Cartography) - A declarative Auto Layout DSL for Swift :large_orange_diamond:
* [AutoLayoutPlus](https://github.com/ruipfcosta/AutoLayoutPlus) - A bit of steroids for AutoLayout, powered by Swift. :large_orange_diamond:
* [Neon](https://github.com/mamaral/Neon) - A powerful Swift programmatic UI layout framework. :large_orange_diamond:
* [MisterFusion](https://github.com/szk-atmosphere/MisterFusion) - A Swift DSL for AutoLayout. It is the extremely clear, but concise syntax, in addition, can be used in both Swift and Objective-C.
* [SwiftBox](https://github.com/joshaber/SwiftBox) - Flexbox in Swift, using Facebook's css-layout. :large_orange_diamond:
* [ManualLayout](https://github.com/isair/ManualLayout) - Easy to use and flexible library for manually laying out views and layers for iOS and tvOS. Supports AsyncDisplayKit. :large_orange_diamond:[e]
* [Stevia](https://github.com/s4cha/Stevia) - Elegant view layout for iOS. :large_orange_diamond:
* [Manuscript](https://github.com/floriankrueger/Manuscript) - AutoLayoutKit in pure Swift. :large_orange_diamond:
* [FDTemplateLayoutCell](https://github.com/forkingdog/UITableView-FDTemplateLayoutCell) - Template auto layout cell for automatically UITableViewCell height calculating
* [SwiftAutoLayout](https://github.com/indragiek/SwiftAutoLayout) - Tiny Swift DSL for Autolayout :large_orange_diamond:
* [FormationLayout](https://github.com/evan-liu/FormationLayout) - Work with auto layout and size classes easily. :large_orange_diamond:
* [SwiftyLayout](https://github.com/fhisa/SwiftyLayout) - Lightweight declarative auto-layout framework for Swift :large_orange_diamond:
* [Swiftstraints](https://github.com/Skyvive/Swiftstraints) - Auto Layout In Swift Made Easy :large_orange_diamond:
* [SwiftBond](https://github.com/SwiftBond/Bond) - Bond is a Swift binding framework that takes binding concepts to a whole new level. It's simple, powerful, type-safe and multi-paradigm. :large_orange_diamond:
* [Restraint](https://github.com/puffinsupply/Restraint) - Minimal Auto Layout in Swift :large_orange_diamond:

### Localization
 * [Hodor](https://github.com/Aufree/Hodor) - Simple solution to localize your iOS App.
 * [Swifternalization](https://github.com/tomkowz/Swifternalization) - Localize iOS apps in a smarter way using JSON files. Swift framework. :large_orange_diamond:
 * [Rubustrings](https://github.com/dcordero/Rubustrings) - Check the format and consistency of Localizable.strings files
 * [BartyCrouch](https://github.com/Flinesoft/BartyCrouch) - Incrementally update your Storyboard localizations with ease. :large_orange_diamond:
 * [Lin](https://github.com/questbeat/Lin) - Xcode plugin that provides auto-completion for NSLocalizedString.
 * [Localize-Swift](https://github.com/marmelroy/Localize-Swift) - Swift 2.0 friendly localization and i18n with in-app language switching :large_orange_diamond:
 * [LocalizedView](https://github.com/darkcl/LocalizedView) - Setting up application specific localized string within Xib file.

### Logging
 * [CleanroomLogger](https://github.com/emaloney/CleanroomLogger) - A configurable and extensible Swift-based logging API that is simple, lightweight and performant. :large_orange_diamond:
 * [CocoaLumberjack](https://github.com/CocoaLumberjack/CocoaLumberjack) - A fast & simple, yet powerful & flexible logging framework for Mac and iOS.
 * [NSLogger](https://github.com/fpillet/NSLogger) - a high perfomance logging utility which displays traces emitted by client applications running on Mac OS X, iOS and Android.
 * [Aardvark](https://github.com/square/Aardvark/) - A performant logging framework that makes it dead simple to create actionable bug reports on iOS.
 * [BlockTypeDescription](https://github.com/conradev/BlockTypeDescription) - Show type signatures when logging blocks.
 * [QorumLogs](https://github.com/goktugyil/QorumLogs) — Swift Logging Utility for Xcode & Google Docs. :large_orange_diamond:
 * [Log](https://github.com/delba/Log) - A logging tool with built-in themes, formatters, and a nice API to define your owns. :large_orange_diamond:
 * [Rainbow](https://github.com/onevcat/Rainbow) - Delightful console output for Swift developers. :large_orange_diamond:
 * [KZLinkedConsole](https://github.com/krzysztofzablocki/KZLinkedConsole) - Clickable links in your Xcode console, so you never wonder which class logged the message. http://merowing.info :large_orange_diamond:
 * [SwiftyBeaver](https://github.com/SwiftyBeaver/SwiftyBeaver) - Colorful, lightweight & fast logging in Swift 2 :large_orange_diamond:
 * [SwiftyTextTable](https://github.com/scottrhoyt/SwiftyTextTable) - A lightweight tool for generating text tables. :large_orange_diamond:
 * [Watchdog](https://github.com/wojteklu/Watchdog) - Class for logging excessive blocking on the main thread :large_orange_diamond:
 * [XCGLogger](https://github.com/DaveWoodCom/XCGLogger) - A debug log framework for use in Swift projects. Allows you to log details to the console (and optionally a file), just like you would have with NSLog or println, but with additional information, such as the date, function name, filename and line number. :large_orange_diamond:
 * [puree](https://github.com/cookpad/puree-ios) - A log collector for iOS :large_orange_diamond:
 * [AFNetworkActivityLogger](https://github.com/AFNetworking/AFNetworkActivityLogger) - AFNetworking 2.0 Extension for Network Request Logging
 * [Colors](https://github.com/icodeforlove/Colors) - A pure Swift library for using ANSI codes. Basically makes command-line coloring and styling very easy! :large_orange_diamond:[e]
 * [Loggerithm](https://github.com/honghaoz/Loggerithm) - A lightweight Swift logger, uses `print` in development and `NSLog` in production. Support colourful and formatted output. :large_orange_diamond:
 * [CleanroomASL](https://github.com/emaloney/CleanroomASL) - A Swift-based API for reading from & writing to the Apple System Log (more commonly known somewhat inaccurately as "the console") :large_orange_diamond:

### Maps
 * [Route-me](https://github.com/route-me/route-me) - Open source map library for iOS.
 * [NAMapKit](https://github.com/neilang/NAMapKit) - Allows you to use custom maps in iphone applications and attempts to mimics some of the behaviour of the MapKit framework.
 * [Mapbox GL](https://github.com/mapbox/mapbox-gl-native) - An OpenGL renderer for Mapbox Vector Tiles with SDK bindings for iOS.
 * [CMMapLauncher](https://github.com/citymapper/CMMapLauncher) - iOS library that makes it quick and easy to show directions in various mapping applications.
 * [GEOSwift](https://github.com/andreacremaschi/GEOSwift) - The Swift Geographic Engine. :large_orange_diamond:

### Media
##### Audio
 * [AudioBus](https://developer.audiob.us/) - Add Next Generation Live App-to-App Audio Routing
 * [AudioKit](https://github.com/audiokit/AudioKit) - A powerful toolkit for synthesizing, processing, and analyzing sounds.
 * [EZAudio](https://github.com/syedhali/EZAudio) - An iOS/OSX audio visualization framework built upon Core Audio useful for anyone doing real-time, low-latency audio processing and visualizations.
 * [novocaine](https://github.com/alexbw/novocaine) - Painless high-performance audio on iOS and Mac OS X.
 * [QHSpeechSynthesizerQueue](https://github.com/quentinhayot/QHSpeechSynthesizerQueue) - Queue management system for AVSpeechSynthesizer (iOS Text to Speech).
 * [StreamingKit](https://github.com/tumtumtum/StreamingKit) - A fast and extensible gapless AudioPlayer/AudioStreamer for OSX and iOS.
 * [sound-fader-ios](https://github.com/evgenyneu/sound-fader-ios) - A sound fader for AVAudioPlayer written in Swift. :large_orange_diamond:
 * [Chirp](https://github.com/trifl/Chirp) - The easiest way to prepare, play, and remove sounds in your Swift app! :large_orange_diamond:
 * [Beethoven](https://github.com/vadymmarkov/Beethoven) - An audio processing Swift library for pitch detection of musical signals. :large_orange_diamond:
 * [Jukebox](https://github.com/teodorpatras/Jukebox) - Player for streaming local and remote audio files. Written in Swift. :large_orange_diamond:
 * [AudioPlayerSwift](https://github.com/tbaranes/AudioPlayerSwift) - AudioPlayer is a simple class for playing audio (basic and advanced usage) in iOS, OS X and tvOS apps :large_orange_diamond:
 * [AudioPlayer](https://github.com/delannoyk/AudioPlayer) - AudioPlayer is syntax and feature sugar over AVPlayer. It plays your audio files (local & remote). :large_orange_diamond:
 * [TuningFork](https://github.com/comyarzaheri/TuningFork) - A Simple Tuner for iOS :large_orange_diamond::black_circle:
 * [MusicKit](https://github.com/benzguo/MusicKit) - A framework for composing and transforming music in Swift :large_orange_diamond:
 * [SubtleVolume](https://github.com/andreamazz/SubtleVolume) - Replace the system volume popup with a more subtle indicator. :large_orange_diamond:

##### Image
 * [GPU Image](https://github.com/BradLarson/GPUImage) - An open source iOS framework for GPU-based image and video processing.
 * [UIImage DSP](https://github.com/gdawg/uiimage-dsp) - IOS UIImage processing functions using the vDSP/Accelerate framework for speed.
 * [QR Code Scanner](http://www.appcoda.com/qr-code-ios-programming-tutorial/) - QR Code implementation.
 * [AsyncImageView](https://github.com/nicklockwood/AsyncImageView) - Simple extension of UIImageView for loading and displaying images asynchronously without lock up the UI.
 * [SDWebImage](https://github.com/rs/SDWebImage) - Asynchronous image downloader with cache support with an UIImageView category.
 * [DFImageManager](https://github.com/kean/DFImageManager) - Modern framework for fetching images from various sources. Zero config yet immense customization and extensibility. Uses NSURLSession.
 * [MapleBacon](https://github.com/zalando/MapleBacon) - An image download and caching library for iOS written in Swift. :large_orange_diamond:
 * [NYTPhotoViewer](https://github.com/NYTimes/NYTPhotoViewer) - Slideshow and image viewer.
 * [IDMPhotoBrowser](https://github.com/ideaismobile/IDMPhotoBrowser) - Photo Browser / Viewer.
 * [JTSImageViewController](https://github.com/jaredsinclair/JTSImageViewController) - Interactive iOS image viewer.
 * [Concorde](https://github.com/contentful-labs/Concorde/) - Download and decode progressive JPEGs.
 * [TOCropViewController](https://github.com/TimOliver/TOCropViewController) - A view controller that allows users to crop UIImage objects.
 * [YXTMotionView](https://github.com/hanton/YXTMotionView) - A custom image view that implements device motion scrolling.
 * [PINRemoteImage](https://github.com/pinterest/PINRemoteImage) - A thread safe, performant, feature rich image fetcher.
 * [SABlurImageView](https://github.com/szk-atmosphere/SABlurImageView) - Easily Adding Animated Blur/Unblur Effects To An Image. :large_orange_diamond:
 * [FastImageCache](https://github.com/path/FastImageCache) - iOS library for quickly displaying images while scrolling.
 * [BKAsciiImage](https://github.com/bkoc/BKAsciiImage) - A library to render UIImage as ASCII art
 * [AlamofireImage](https://github.com/Alamofire/AlamofireImage) - An image component library for Alamofire. :large_orange_diamond:
 * [Nuke](https://github.com/kean/Nuke) - Advanced framework for managing images :large_orange_diamond:
 * [FlagKit](https://github.com/madebybowtie/FlagKit) - Beautiful flag icons for usage in apps and on the web. :large_orange_diamond:
 * [YYWebImage](https://github.com/ibireme/YYWebImage) - Asynchronous image loading framework (supports WebP, APNG, GIF).
 * [RSKImageCropper](https://github.com/ruslanskorb/RSKImageCropper) - An image cropper for iOS like in the Contacts app with support for landscape orientation.
 * [Silo](https://github.com/josejuanqm/Silo) - Image loading framework with loaders. :large_orange_diamond:
 * [Ody](https://github.com/josejuanqm/Ody) - Ody is an easy to use random image generator built with Swift, Perfect for placeholders. :large_orange_diamond:
 * [Banana](https://github.com/gauravkatoch007/banana) - Image slider with very simple interface. :large_orange_diamond:
 * [JDSwiftAvatarProgress](https://github.com/JellyDevelopment/JDSwiftAvatarProgress) - Easy customizable avatar image asynchronously with progress bar animated :large_orange_diamond:
 * [Kingfisher](https://github.com/onevcat/Kingfisher) - A lightweight and pure Swift implemented library for downloading and caching image from the web. :large_orange_diamond:
 * [EBPhotoPages](https://github.com/EddyBorja/EBPhotoPages) - A photo gallery for iOS with a modern feature set. Similar features as the Facebook photo browser.
 * [UIImageView-BetterFace-Swift](https://github.com/croath/UIImageView-BetterFace-Swift) - The Swift version of https://github.com/croath/UIImageView-BetterFace :large_orange_diamond:
 * [KFSwiftImageLoader](https://github.com/kiavashfaisali/KFSwiftImageLoader) - An extremely high-performance, lightweight, and energy-efficient pure Swift async web image loader with memory and disk caching for iOS and  Watch. :large_orange_diamond:
 * [Toucan](https://github.com/gavinbunney/Toucan) - Fabulous Image Processing in Swift :large_orange_diamond:
 * [ImageLoaderSwift](https://github.com/hirohisa/ImageLoaderSwift) - A lightweight and fast image loader for iOS written in Swift. :large_orange_diamond:
 * [ImageScout](https://github.com/kaishin/ImageScout) - A Swift implementation of fastimage. Supports PNG, GIF, and JPEG. :large_orange_diamond:
 * [Fusuma](https://github.com/ytakzk/Fusuma) - Instagram-like photo browser and a camera feature with a few line of code in Swift. :large_orange_diamond:
 * [Agrume](https://github.com/JanGorman/Agrume) - A lemony fresh iOS image viewer written in Swift. :large_orange_diamond:
 * [PASImageView](https://github.com/abiaad/PASImageView) - Rounded async imageview downloader lightly cached and written in Swift :large_orange_diamond:
 * [Navi](https://github.com/nixzhu/Navi) - Focus on avatar caching. :large_orange_diamond:
 * [SwiftPhotoGallery](https://github.com/Inspirato/SwiftPhotoGallery) - Simple, fullscreen image gallery with tap, swipe, and pinch gestures. :large_orange_diamond:

##### GIF
 * [YLGIFImage](https://github.com/liyong03/YLGIFImage) - Async GIF image decoder and Image viewer supporting play GIF images. It just use very less memory.
 * [FLAnimatedImage](https://github.com/Flipboard/FLAnimatedImage) - Performant animated GIF engine for iOS
 * [gifu](https://github.com/kaishin/gifu) - Highly performant animated GIF support for iOS in Swift :large_orange_diamond:
 * [AnimatedGIFImageSerialization](https://github.com/mattt/AnimatedGIFImageSerialization) - Complete Animated GIF Support for iOS, with Functions, NSJSONSerialization-style Class, and (Optional) UIImage Swizzling
 * [XAnimatedImage](https://github.com/khaledmtaha/XAnimatedImage) - XAnimatedImage is a performant animated GIF engine for iOS written in Swift based on FLAnimatedImage :large_orange_diamond:
 * [SwiftGif](https://github.com/bahlo/SwiftGif) - :sparkles: A small UIImage extension with gif support :large_orange_diamond:
 * [APNGKit](https://github.com/onevcat/APNGKit) - High performance and delightful way to play with APNG format in iOS. :large_orange_diamond:
 * [YYImage](https://github.com/ibireme/YYImage) - Image framework for iOS to display/encode/decode animated WebP, APNG, GIF, and more.
 * [JWAnimatedImage](https://github.com/wangjwchn/JWAnimatedImage) - A animated GIF engine for iOS in Swift with low memory & cpu usage.:large_orange_diamond:

##### Video
 * [VIMVideoPlayer](https://github.com/vimeo/VIMVideoPlayer) - A simple wrapper around the AVPlayer and AVPlayerLayer classes.
 * [MobilePlayer](https://github.com/mobileplayer/mobileplayer-ios) - A powerful and completely customizable media player for iOS.
 * [XCDYouTubeKit](https://github.com/0xced/XCDYouTubeKit) - YouTube video player for iOS, tvOS and OS X
 * [AVAnimator](http://www.modejong.com/AVAnimator/) - An open source iOS native library that makes it easy to implement non-trivial video/audio enabled apps.
 * [360 VR Player](https://github.com/hanton/HTY360Player) - A open source, ad-free, native and universal 360 degree panorama video player for iOS.
 * [Periscope VideoViewController](https://github.com/gontovnik/Periscope-VideoViewController) - Video view controller with Periscope fast rewind control :large_orange_diamond:
 * [SSVideoPlayer](https://github.com/immrss/SSVideoPlayer) - A video player that support both local and network resource.
 * [MHVideoPhotoGallery](https://github.com/mariohahn/MHVideoPhotoGallery) - A Photo and Video Gallery
 * [PlayerView](https://github.com/davidlondono/PlayerView) - Player View is a delegated view using AVPlayer of Swift :large_orange_diamond:
 * [simple360player](https://github.com/Aralekk/simple360player_iOS) - Free & ad-free 360 VR Video Player. Flat or Stereoscopic. In Swift 2. :large_orange_diamond:

##### PDF
* [Reader](https://github.com/vfr/Reader) - PDF Reader Core for iOS.
* [UIView 2 PDF](https://github.com/RobertAPhillips/UIView_2_PDF) - PDF generator using UIViews or UIViews with an associated XIB
* [FolioReaderKit](https://github.com/FolioReader/FolioReaderKit) - A Swift ePub reader and parser framework for iOS. :large_orange_diamond:
* [PDFGenerator](https://github.com/sgr-ksmt/PDFGenerator) - A simple Generator of PDF in Swift. Generate PDF from view(s) or image(s). :large_orange_diamond:
* [SimplePDF](https://github.com/nRewik/SimplePDF) - Create a simple PDF effortlessly. :large_orange_diamond:

### Messaging

Also see [push notifications](#push-notifications)

 * [LayerKit](https://github.com/layerhq/releases-ios) - iOS SDK for Layer, the easiest way to add in-app messaging (text, photos, videos, data) to any mobile or web application.
 * [Twilio](https://www.twilio.com/) - Power modern communications. Build the next generation of voice and SMS applications.
 * [Plivo](https://www.plivo.com/) - SMS API, Voice API, & Global Carrier Provider.
 * [XMPPFramework](https://github.com/robbiehanson/XMPPFramework) - An XMPP Framework in Objective-C for Mac and iOS.
 * [Chatto](https://github.com/badoo/Chatto) - A lightweight framework to build chat applications, made in Swift :large_orange_diamond:
 * [JSQMessagesViewController](https://github.com/jessesquires/JSQMessagesViewController) - An elegant messages UI library for iOS.
 * [Smooch](https://smooch.io) - Simple, lightweight SDKs and interfaces that enable customer messaging inside your apps and websites.

### Machine Learning
 * [Swift-AI](https://github.com/collinhundley/Swift-AI) - Highly optimized Artificial Intelligence and Machine Learning library written in Swift. :large_orange_diamond:
 * [Swift-Brain](https://github.com/vlall/Swift-Brain) - Artificial Intelligence/Machine Learning data structures and Swift algorithms for future iOS development. Bayes theorem, Neural Networks, and more AI. :large_orange_diamond:

### Networking
 * [AFNetworking](https://github.com/AFNetworking/AFNetworking) - A delightful iOS and OS X networking framework.
 * [RestKit](https://github.com/RestKit/RestKit) - RestKit is an Objective-C framework for iOS that aims to make interacting with RESTful web services simple, fast and fun.
 * [FSNetworking](https://github.com/foursquare/FSNetworking) - Foursquare iOS networking library.
 * [ASIHTTPRequest](https://github.com/pokeb/asi-http-request) - Easy to use CFNetwork wrapper for HTTP requests, Objective-C, Mac OS X and iPhone.
 * [Overcoat](https://github.com/Overcoat/Overcoat) - Small but powerful library that makes creating REST clients simple and fun.
 * [ROADFramework](https://github.com/epam/road-ios-framework) - Attributed-oriented approach for interacting with web services. The framework has built-in json and xml serialization for requests and responses and can be easily extensible.
 * [MBNetworkMonitor](https://github.com/emaloney/MBToolbox/blob/master/Code/Network/MBNetworkMonitor.h) - A modern replacement for Apple's `Reachability` class that uses CoreTelephony to report more [information about the user's network connection](https://rawgit.com/emaloney/MBToolbox/master/Documentation/html/Classes/MBNetworkMonitor.html).
 * [Alamofire](https://github.com/Alamofire/Alamofire) - Alamofire is an HTTP networking library written in Swift, from the creator of AFNetworking. :large_orange_diamond:
 * [Transporter](https://github.com/nghialv/Transporter) - A tiny library makes uploading and downloading easier. :large_orange_diamond:
 * [CDZPinger](https://github.com/cdzombak/CDZPinger) - Easy-to-use ICMP Ping.
 * [NSRails](https://github.com/dingbat/nsrails) - Map client-side objects/classes to remote rest api objects/orm
 * [NKMultipeer](https://github.com/nathankot/NKMultipeer) - A testable abstraction over multipeer connectivity. :large_orange_diamond:
 * [CocoaAsyncSocket](https://github.com/robbiehanson/CocoaAsyncSocket) - Asynchronous socket networking library for Mac and iOS.
 * [Siesta](https://bustoutsolutions.github.io/siesta/) - Elegant abstraction for RESTful resources that untangles stateful messes. An alternative to callback- and delegate-based networking. :large_orange_diamond:
 * [Reachability.swift](https://github.com/ashleymills/Reachability.swift) - Replacement for Apple's Reachability re-written in Swift with closures :large_orange_diamond:
 * [NetworkEye](https://github.com/coderyi/NetworkEye) - a iOS network debug library, It can monitor HTTP requests within the App and displays information related to the request.
 * [Netfox](https://github.com/kasketis/netfox) - A lightweight, one line setup, iOS network debugging library! :large_orange_diamond:
 * [OctopusKit](https://github.com/icoco/OctopusKit) - A simplicity but graceful solution for invoke RESTful web service APIs.
 * [Moya](https://github.com/Moya/Moya) - Network abstraction layer written in Swift. :large_orange_diamond:
 * [TWRDownloadManager](https://github.com/chasseurmic/TWRDownloadManager) - A modern download manager based on NSURLSession to deal with asynchronous downloading, management and persistence of multiple files.
 * [HappyDns](https://github.com/qiniu/happy-dns-objc) - A Dns library, support custom dns server, dnspod httpdns. Only support A record.
 * [Bridge](https://github.com/rawrjustin/Bridge) - A simple extensible typed networking library. Intercept and process/alter requests and responses easily. :large_orange_diamond:
 * [TRON](https://github.com/MLSDev/TRON) - Lightweight network abstraction layer, written on top of Alamofire and SwiftyJSON :large_orange_diamond:
 * [EVCloudKitDao](https://github.com/evermeer/EVCloudKitDao) - Simplified access to Apple's CloudKit :large_orange_diamond:
 * [EVURLCache](https://github.com/evermeer/EVURLCache) - a NSURLCache subclass for handling all web requests that use NSURLRequest :large_orange_diamond:
 * [ResponseDetective](https://github.com/netguru/ResponseDetective) - Sherlock Holmes of the networking layer :large_orange_diamond:
 * [Pitaya](https://github.com/johnlui/Pitaya) - A Swift HTTP / HTTPS networking library just incidentally execute on machines :large_orange_diamond:
 * [Just](https://github.com/JustHTTP/Just) - Swift HTTP for Humans :large_orange_diamond:
 * [agent](https://github.com/hallas/agent) - Minimalistic Swift HTTP request agent for iOS and OS X :large_orange_diamond:
 * [Reach](https://github.com/Isuru-Nanayakkara/Reach) - A simple class to check for internet connection availability in Swift. :large_orange_diamond:
 * [SwiftHTTP](https://github.com/daltoniam/SwiftHTTP) - Thin wrapper around NSURLSession in swift. Simplifies HTTP requests. :large_orange_diamond:
 * [Netdiag](https://github.com/qiniu/iOS-netdiag) - A network diagnosis library. Support Ping/TcpPing/Rtmp/TraceRoute/DNS/external IP/external DNS.
 * [AFNetworkingHelper](https://github.com/betacraft/AFNetworkingHelper) - A custom wrapper over AFNetworking library that we use inside RC extensively
 * [NetKit](https://github.com/azizuysal/NetKit) - A Concise HTTP Framework in Swift. :large_orange_diamond:
 * [RealReachability](https://github.com/dustturtle/RealReachability) - We need to observe the REAL reachability of network. That's what RealReachability do.
 * [MonkeyKing](https://github.com/nixzhu/MonkeyKing) - MonkeyKing helps you post messages to Chinese Social Networks. :large_orange_diamond:
 * [NetworkKit](https://github.com/imex94/NetworkKit) - Lightweight Networking and Parsing framework made for iOS, Mac, WatchOS and tvOS. :large_orange_diamond:
 * [APIKit](https://github.com/ishkawa/APIKit) - A networking library for building type safe web API client in Swift. :large_orange_diamond:

#### Email

 * [Mail Core 2](https://github.com/MailCore/mailcore2) - MailCore 2 provide a simple and asynchronous API to work with e-mail protocols IMAP, POP and SMTP.

### Push Notifications
 * [Orbiter](https://github.com/mattt/Orbiter) - Push Notification Registration for iOS.
 * [PEM](https://github.com/fastlane/fastlane/tree/master/pem) - Automatically generate and renew your push notification profiles.
 * [Knuff](https://github.com/KnuffApp/Knuff) - The debug application for Apple Push Notification Service (APNS).

#### Push Notification Providers

Most of these are paid services, some have free tiers.

 * [Urban Airship](https://www.urbanairship.com/products/engage#push-messages)
 * [Growth Push](https://growthpush.com) - Popular in Japan.
 * [Appboy](https://www.appboy.com)
 * [Batch](https://batch.com)
 * [Boxcar](https://boxcar.io/developer)
 * [Carnival](http://www.carnival.io)
 * [Catapush](https://www.catapush.com)
 * [Netmera](http://www.netmera.com)
 * [OneSignal](https://www.onesignal.com) - Free.
 * [PushBots](https://www.pushbots.com)
 * [Pushwoosh](https://www.pushwoosh.com)

### Passbook
 * [passbook](https://github.com/frozon/passbook) - Passbook gem let's you create pkpass for passbook iOS 6+.
 * [Dubai](https://github.com/nomad/dubai) - Generate and Preview Passbook Passes.
 * [Passkit](https://passkit.com) - Design, Create and validate Passbook Passes.

### Permissions
* [PermissionScope](https://github.com/nickoneill/PermissionScope) - Intelligent iOS permissions UI and unified API (Supports Location, Notifications, Camera, Contacts, Calendar, Photos, Microphone, BT, Activity Monitoring, HealthKit and CloudKit). :large_orange_diamond:
* [Proposer](https://github.com/nixzhu/Proposer) - Make permission request easier (Supports Camera, Photos, Microphone, Contacts, Location). :large_orange_diamond:
* [ICanHas](https://github.com/wircho/ICanHas) - Simplifies iOS user permission requests (Supports location, push notifications, camera, contacts, calendar, photos). :large_orange_diamond:
* [VWWPermissionKit](https://github.com/zakkhoyt/VWWPermissionKit) - A visual permission manager for iOS.
* [ISHPermissionKit](https://github.com/iosphere/ISHPermissionKit) - A unified way for iOS apps to request user permissions.
* [JLPermissions](https://github.com/jlaws/JLPermissions) - An iOS pre-permissions utility that lets developers ask users on their own dialog for calendar, contacts, location, photos, reminders, twitter, push notifications and more, before making the system-based permission request.
* [ClusterPrePermissions](https://github.com/clusterinc/ClusterPrePermissions) - Reusable pre-permissions utility that lets developers ask users for access in their own dialog, before making the system-based request.
* [Permission](https://github.com/delba/Permission) - Ask for iOS permissions through a single, uniform interface. :large_orange_diamond:
* [STLocationRequest](https://github.com/SvenTiigi/STLocationRequest) - A simple and elegant 3D-Flyover location request screen written Swift. :large_orange_diamond:

### Regex
 * [Regex](https://github.com/sharplet/Regex) - A Swift µframework providing an NSRegularExpression-backed Regex type :large_orange_diamond:
 * [SwiftRegex](https://github.com/kasei/SwiftRegex) - Perl-like regex =~ operator for Swift :large_orange_diamond:
 * [PySwiftyRegex](https://github.com/cezheng/PySwiftyRegex) - Easily deal with Regex in Swift in a Pythonic way :large_orange_diamond:

### Security
 * [UICKeyChainStore](https://github.com/kishikawakatsumi/UICKeyChainStore) - UICKeyChainStore is a simple wrapper for Keychain on iOS.
 * [cocoapods-keys](https://github.com/orta/cocoapods-keys) - A key value store for storing environment and application keys.
 * [Valet](https://github.com/square/Valet) - Securely store data in the iOS or OS X Keychain without knowing a thing about how the Keychain works.
 * [Locksmith](https://github.com/matthewpalmer/Locksmith) - A powerful, protocol-oriented library for working with the keychain in Swift. :large_orange_diamond:
 * [simple-touch](https://github.com/simple-machines/simple-touch) - Very simple swift wrapper for Biometric Authentication Services (Touch ID) on iOS.
 * [Obfuscator-iOS](https://github.com/pjebs/Obfuscator-iOS) - String Obfuscation for app's executable file
 * [KeychainAccess](https://github.com/kishikawakatsumi/KeychainAccess) - Simple Swift wrapper for Keychain that works on iOS and OS X :large_orange_diamond:[e]
 * [Themis](https://github.com/cossacklabs/themis) - High-level crypto library, providing basic asymmetric encryption, secure messaging with forward secrecy and secure data storage, supports iOS/OS X, Android and different server side platforms.
 * [Keychain](https://github.com/hyperoslo/Keychain) - Because you should care... about the security... of your shit. :large_orange_diamond:
 * [CryptoSwift](https://github.com/krzyzanowskim/CryptoSwift) - Crypto related functions and helpers for Swift implemented in Swift programming language :large_orange_diamond:
 * [SwiftPasscodeLock](https://github.com/yankodimitrov/SwiftPasscodeLock) - An iOS passcode lock with TouchID authentication written in Swift. :large_orange_diamond:
 * [SwiftSSL](https://github.com/SwiftP2P/SwiftSSL) - An Elegant crypto toolkit in Swift. :large_orange_diamond:
 * [SwiftyRSA](https://github.com/TakeScoop/SwiftyRSA) - RSA public/private key encryption in Swift :large_orange_diamond:
 * [EnigmaKit](https://github.com/mikaoj/EnigmaKit) - Enigma encryption in Swift :large_orange_diamond:

### Text
 * [Twitter Text Obj](https://github.com/twitter/twitter-text) - An Objective-C implementation of Twitter's text processing library.
 * [Nimbus](https://github.com/jverkoey/nimbus) - Nimbus is a toolkit for experienced iOS software designers.
 * [NSStringEmojize](https://github.com/diy/nsstringemojize) - A category on NSString to convert Emoji Cheat Sheet codes to their equivalent Unicode characters.
 * [MMMarkdown](https://github.com/mdiep/MMMarkdown) - An Objective-C static library for converting Markdown to HTML.
 * [DTCoreText](https://github.com/Cocoanetics/DTCoreText) - Methods to allow using HTML code with CoreText.
 * [DTRichTextEditor](https://github.com/Cocoanetics/DTRichTextEditor) - A rich-text editor for iOS.
 * [NBEmojiSearchView](https://github.com/neerajbaid/NBEmojiSearchView) - A searchable emoji dropdown view that can be integrated with a text control
 * [ios-fontawesome](https://github.com/alexdrone/ios-fontawesome) - NSString+FontAwesome.
 * [Pluralize.swift](https://github.com/joshualat/Pluralize.swift) - Great Swift String Pluralize Extension :large_orange_diamond:[e]
 * [RichEditorView](https://github.com/cjwirth/RichEditorView) - RichEditorView is a simple, modular, drop-in UIView subclass for Rich Text Editing. :large_orange_diamond:
 * [Money](https://github.com/danthorpe/Money) - Swift value types for working with money & currency :large_orange_diamond:
 * [PhoneNumberKit](https://github.com/marmelroy/PhoneNumberKit) - A Swift framework for parsing, formatting and validating international phone numbers. Inspired by Google's libphonenumber. :large_orange_diamond:
 * [YYText](https://github.com/ibireme/YYText) - Powerful text framework for iOS to display and edit rich text.
 * [FontAwesome.swift](https://github.com/thii/FontAwesome.swift) - Use FontAwesome in your Swift projects. :large_orange_diamond:
 * [Format](https://github.com/marmelroy/Format) - A Swift Formatter Kit. :large_orange_diamond:
 * [Tribute](https://github.com/zats/Tribute) - Programmatic creation of NSAttributedString doesn't have to be a pain :large_orange_diamond:
 * [EmojiKit](https://github.com/dasmer/EmojiKit) - Effortless emoji-querying in Swift :large_orange_diamond:
 * [Roman](https://github.com/nvzqz/Roman) - Seamless Roman numeral conversion in Swift. :large_orange_diamond:
 * [ZSSRichTextEditor](https://github.com/nnhubbard/ZSSRichTextEditor) - A beautiful rich text WYSIWYG editor for iOS with a syntax highlighted source view :large_orange_diamond:
 * [pangu.Objective-C](https://github.com/Cee/pangu.objective-c) - Paranoid text spacing in Objective-C.
 * [SwiftString](https://github.com/amayne/SwiftString) - A comprehensive, lightweight string extension for Swift :large_orange_diamond:[e]
 * [Marklight](https://github.com/macteo/Marklight) - Markdown syntax highlighter for iOS :large_orange_diamond:
 * [SwiftFontName](https://github.com/morizotter/SwiftFontName) - OS font complements library. Localized font supported :large_orange_diamond:
 * [MarkdownTextView](https://github.com/indragiek/MarkdownTextView) - Rich Markdown editing control for iOS :large_orange_diamond:
 * [FontBlaster](https://github.com/ArtSabintsev/FontBlaster) - Programmatically load custom fonts into your iOS app. :large_orange_diamond:

### Walkthrough / Intro / Tutorial
 * [Onboard](https://github.com/mamaral/Onboard) - Easily create a beautiful and engaging onboarding experience with only a few lines of code.
 * [EAIntroView](https://github.com/ealeksandrov/EAIntroView) - Highly customizable drop-in solution for introduction views.
 * [MYBlurIntroductionView](https://github.com/MatthewYork/MYBlurIntroductionView) - A super-charged version of MYIntroductionView for building custom app introductions and tutorials.
 * [BWWalkthrough](https://github.com/ariok/BWWalkthrough) - A class to build custom walkthroughs for your iOS App. :large_orange_diamond:
 * [GHWalkThrough](https://github.com/GnosisHub/GHWalkThrough) - A UICollectionView backed drop-in component for introduction views.
 * [ICETutorial](https://github.com/icepat/ICETutorial) - A nice tutorial like the one introduced in the Path 3.X App.
 * [JazzHands](https://github.com/IFTTT/JazzHands) - Jazz Hands is a simple keyframe-based animation framework for UIKit. Animations can be controlled via gestures, scroll views, KVO, or ReactiveCocoa.
 * [RazzleDazzle](https://github.com/IFTTT/RazzleDazzle) - A simple keyframe-based animation framework for iOS, written in Swift. Perfect for scrolling app intros. :large_orange_diamond:
 * [Instructions](https://github.com/ephread/Instructions) - Easily add customizable coach marks into you iOS project. :large_orange_diamond:
 * [SwiftyWalkthrough](https://github.com/ruipfcosta/SwiftyWalkthrough) - The easiest way to create a great walkthrough experience in your apps, powered by Swift. :large_orange_diamond:
 * [Gecco](https://github.com/yukiasai/Gecco) - Spotlight view for iOS. :large_orange_diamond:
 * [VideoSplashKit](https://github.com/movielala/VideoSplashKit) - Video based UIViewController :large_orange_diamond:
 * [Presentation](https://github.com/hyperoslo/Presentation) - Presentation helps you to make tutorials, release notes and animated pages. :large_orange_diamond:
 * [AMPopTip](https://github.com/andreamazz/AMPopTip) - An animated popover that pops out a given frame, great for subtle UI tips and onboarding.

### URL Scheme
 * [WAAppRouting](https://github.com/Wasappli/WAAppRouting) - iOS routing done right. Handles both URL recognition and controller displaying with parsed parameters. All in one line, controller stack preserved automatically!
 * [DeepLinkKit](https://github.com/button/DeepLinkKit) - A splendid route-matching, block-based way to handle your deep links.
 * [IntentKit](https://github.com/intentkit/IntentKit) - An easier way to handle third-party URL schemes in iOS apps.
 * [JLRoutes](https://github.com/joeldev/JLRoutes) - URL routing library for iOS with a simple block-based API.
 * [IKRouter](https://github.com/IanKeen/IKRouter) - URLScheme router than supports auto creation of UIViewControllers for associated url parameters to allow creation of navigation stacks :large_orange_diamond:
 * [Compass](https://github.com/hyperoslo/Compass) - Compass helps you setup a central navigation system for your application :large_orange_diamond:
 * [Appz](https://github.com/SwiftKitz/Appz) - Easily launch and deeplink into external applications, falling back to web if not installed. :large_orange_diamond:
 * [URLNavigator](https://github.com/devxoul/URLNavigator) - :boat: Elegant URL Routing for Swift :large_orange_diamond:

### UI
 * [ActionSheetPicker-3.0](https://github.com/skywinder/ActionSheetPicker-3.0/) - Quickly reproduce the dropdown UIPickerView / ActionSheet functionality on iOS.
 * [FlatUIKit](https://github.com/Grouper/FlatUIKit) - A collection of awesome flat UI components for iOS.
 * [BetweenKit](https://github.com/ice3-software/between-kit) - A robust drag-and-drop framework for iOS.
 * [MDCSwipeToChoose](https://github.com/modocache/MDCSwipeToChoose) - Swipe to "like" or "dislike" any view, just like Tinder.app. Build a flashcard app, a photo viewer, and more, in minutes, not hours!
 * [JLToast](https://github.com/devxoul/JLToast) - Toast for iOS with very simple interface. :large_orange_diamond:
 * [BLKFlexibleHeightBar](https://github.com/bryankeller/BLKFlexibleHeightBar) - Create condensing header bars like those seen in the Facebook, Square Cash, and Safari iOS apps.
 * [SDevIconFonts](https://github.com/0x73/SDevIconFonts) - Fontawesome, Iconic, Ionicons, Octicon porting for swift. :large_orange_diamond:
 * [Motif](https://github.com/erichoracek/Motif) - A lightweight and customizable JSON stylesheet framework for iOS.
 * [AsyncDisplayKit](https://github.com/facebook/AsyncDisplayKit/) - AsyncDisplayKit is an iOS framework that keeps even the most complex user interfaces smooth and responsive.
 * [AMTagListView](https://github.com/andreamazz/AMTagListView) - UIScrollView subclass that allows to add a list of highly customizable tags.
 * [MotionBlur](https://github.com/fastred/MotionBlur) - MotionBlur allows you to add motion blur effect to iOS animations.
 * [GaugeKit](https://github.com/skywinder/GaugeKit) - Customizable gauges. Easy reproduce Apple's style gauges. :large_orange_diamond:
 * [SVWebViewController](https://github.com/TransitApp/SVWebViewController) - A drop-in inline browser for your iOS app.
 * [SwiftWebVC](https://github.com/meismyles/SwiftWebVC) - A Swift implementation of SVWebViewController - a drop-in inline browser for your iOS app. :large_orange_diamond:
 * [MVMaterialView](https://github.com/mrugrajsinh/MVMaterialView) - Subclass of UIControls and UIButton to mimic Ripple effect of Material Design concept.
 * [Atlas](https://github.com/layerhq/Atlas-iOS) - A library of native iOS messaging user interface components for Layer.
 * [TisprCardStack](https://github.com/tispr/tispr-card-stack) - Library that allows to have cards UI. :large_orange_diamond:
 * [SAHistoryNavigationViewController](https://github.com/szk-atmosphere/SAHistoryNavigationViewController) - SAHistoryNavigationViewController realizes iOS task manager like UI in UINavigationContoller,3D Touch Compatible. :large_orange_diamond:
 * [SAInboxViewController](https://github.com/szk-atmosphere/SAInboxViewController) - UIViewController subclass inspired by "Inbox by google" animated transitioning. :large_orange_diamond:
 * [TLYShyNavBar](https://github.com/telly/TLYShyNavBar) - Unlike all those arrogant UINavigationBar, this one is shy and humble! Easily create auto-scrolling navigation bars!
 * [MZFormSheetPresentationController](https://github.com/m1entus/MZFormSheetPresentationController) - MZFormSheetPresentationController provides an alternative to the native iOS UIModalPresentationFormSheet, adding support for iPhone and additional opportunities to setup controller size and feel form sheet.
 * [AnimatedTransitionGallery](https://github.com/shu223/AnimatedTransitionGallery) - Collection of iOS 7 custom animated transitions using UIViewControllerAnimatedTransitioning protocol.
 * [iCarousel](https://github.com/nicklockwood/iCarousel) - A simple, highly customisable, data-driven 3D carousel for iOS and Mac OS.
 * [FontAwesomeKit](https://github.com/PrideChung/FontAwesomeKit) - Icon font library for iOS. Currently supports Font-Awesome, Foundation icons, Zocial, and ionicons.
 * [Cocoa Controls](https://www.cocoacontrols.com/) - Open source UI components for iOS and OS X.
 * [RAReorderableLayout](https://github.com/ra1028/RAReorderableLayout) - A UICollectionView layout whitch can move item with drag and drop.
 * [HoneycombView](https://github.com/suzuki-0000/HoneycombView) - HoneycombView is the iOS UIView for displaying like Honyecomb layout written by swift. :large_orange_diamond:
 * [tapkulibrary](https://github.com/devinross/tapkulibrary) - tap + haiku = tapku, a well crafted open source iOS framework.
 * [KCHorizontalDial](https://github.com/kciter/KCHorizontalDial) - A horizontal scroll dial like Instagram. :large_orange_diamond:
 * [DAExpandAnimation](https://github.com/ifitdoesntwork/DAExpandAnimation) - A custom modal transition that presents a controller with an expanding effect while sliding out the presenter remnants. :large_orange_diamond:
 * [ScrollPager](https://github.com/aryaxt/ScrollPager) - A scroll pager similar to the one in Flipboard :large_orange_diamond:
 * [ComponentKit](http://componentkit.org/) - A React-Inspired View Framework for iOS, by Facebook.
 * [PMTween](https://github.com/poetmountain/PMTween) - An elegant and flexible tweening library for iOS.
 * [WobbleView](https://github.com/inFullMobile/WobbleView) - WobbleView is an implementation of a recently popular wobble effect for any view in your app. It can be used to easily add dynamics to user interactions and transitions. :large_orange_diamond:
 * [CBZSplashView](https://github.com/callumboddy/CBZSplashView) - Twitter style Splash Screen View. Grows to reveal the Initial view behind.
 * [RKNotificationHub](https://github.com/cwRichardKim/RKNotificationHub) - Make any UIView a full fledged notification center.
 * [EatFit](https://github.com/Yalantis/EatFit) - Eat fit is a component for attractive data representation inspired by Google Fit
 * [CollapsableOptions](https://github.com/rob-nash/CollapsableOptions) - Collapsable table view sections with custom section header views. :large_orange_diamond:
 * [PickerView](https://github.com/filipealva/PickerView) - A customizable alternative to UIPickerView in Swift. :large_orange_diamond:
 * [InteractivePlayerView](https://github.com/AhmettKeskin/InteractivePlayerView) - Custom iOS music player view :large_orange_diamond:
 * [phone-number-picker](https://github.com/hughbe/phone-number-picker) - A simple and easy to use view controller enabling you to enter a phone number with a country code similar to WhatsApp written in Swift :large_orange_diamond:
 * [DLWBouncyView](https://github.com/cute/DLWBouncyView) - BouncyView is an implementation of a recently popular bouncy effect for any view.
 * [EXTView](https://github.com/recruit-mtl/EXTView) - Extended UIView for Interface Builder by using IB_DESIGNABLE and IBInspectable.
 * [JTMaterialSwitch](https://github.com/JunichiT/JTMaterialSwitch) - A customizable switch UI with ripple effect and bounce animations, inspired from Google's Material Design.
 * [KCSelectionDialog](https://github.com/kciter/KCSelectionDialog) - Simple selection dialog. :large_orange_diamond:
 * [SFFocusViewLayout](https://github.com/fdzsergio/SFFocusViewLayout) - UICollectionViewLayout with focused content.
 * [TTGEmojiRate](https://github.com/zekunyan/TTGEmojiRate) - An emoji-liked rating view for iOS, implemented in Swift. :large_orange_diamond:
 * [CardAnimation](https://github.com/seedante/CardAnimation) - Card flipping-style animation :large_orange_diamond:
 * [BEMCheckBox](https://github.com/Boris-Em/BEMCheckBox#sample-app) - Tasteful Checkbox for iOS. (Check box)
 * [HorizontalProgress](https://github.com/AliThink/HorizontalProgress) - Simple horizontal progress bar with animation
 * [TKSwitcherCollection](https://github.com/TBXark/TKSwitcherCollection) - An animate switch collection :large_orange_diamond:
 * [StarryStars](https://github.com/peterprokop/StarryStars) - iOS GUI library for displaying and editing ratings
 * [JRSplitVC](https://github.com/tommypeps/JRSplitVC) - UISplitViewController with adaptative layouts
 * [SevenSwitch](https://github.com/bvogelzang/SevenSwitch) - iOS7 style drop in replacement for UISwitch. :large_orange_diamond:
 * [MPParallaxView](https://github.com/DroidsOnRoids/MPParallaxView) - Apple TV Parallax effect in Swift. :large_orange_diamond:
 * [Splitflap](https://github.com/yannickl/Splitflap) - A simple split-flap display for your Swift applications :large_orange_diamond:
 * [UIScrollView-InfiniteScroll](https://github.com/pronebird/UIScrollView-InfiniteScroll) - UIScrollView infinite scroll category :large_orange_diamond:
 * [EZSwipeController](https://github.com/goktugyil/EZSwipeController) - :point_up_2: UIPageViewController like Snapchat/Tinder/iOS Main Pages :large_orange_diamond:
 * [SWRevealViewController](https://github.com/John-Lluch/SWRevealViewController) - A UIViewController subclass for presenting side view controllers inspired on the FaceBook and Wunderlist apps, done right.
 * [TagCellLayout](https://github.com/riteshhgupta/TagCellLayout) - UICollectionView layout for Tags with Left, Center & Right alignments. :large_orange_diamond:
 * [Koloda](https://github.com/Yalantis/Koloda) - KolodaView is a class designed to simplify the implementation of Tinder like cards on iOS. :large_orange_diamond:
 * [XLActionController](https://github.com/xmartlabs/XLActionController) - Fully customizable and extensible action sheet controller written in Swift. :large_orange_diamond:
 * [FooterPull](https://github.com/rob-nash/FooterPull) - Add paging to your table views with a cool animation.
 * [StackPageView](https://github.com/noppefoxwolf/StackPageView) - Vertical page view with UIViewControllers stacked on the top of each other :large_orange_diamond:
 * [PageControl](https://github.com/kasper-lahti/PageControl) - ● ○ ○ ○ A nice, animated UIPageControl alternative. :large_orange_diamond:
 * [Curry](https://github.com/devinross/curry) - Curry is a framework built to enhance and compliment Foundation and UIKit.
 * [KMNavigationBarTransition](https://github.com/MoZhouqi/KMNavigationBarTransition) - A drop-in universal library makes transition animations smooth between different navigation bar styles while pushing or popping a view controller. :large_orange_diamond:
 * [ElasticTransition](https://github.com/lkzhao/ElasticTransition) - A UIKit custom transition that simulates an elastic drag. Written in Swift. :large_orange_diamond:
 * [Pages](https://github.com/hyperoslo/Pages) - UIPageViewController made simple :large_orange_diamond:
 * [BothamUI](https://github.com/Karumi/BothamUI) - Model View Presenter Framework written in Swift. http://karumi.com :large_orange_diamond:
 * [RainbowNavigation](https://github.com/DanisFabric/RainbowNavigation) - An easy way to change backgroundColor of UINavigationBar when Push & Pop :large_orange_diamond:
 * [DGRunkeeperSwitch](https://github.com/gontovnik/DGRunkeeperSwitch) - Runkeeper design switch control (two part segment control) :large_orange_diamond:
 * [PFStepper](https://github.com/PerfectFreeze/PFStepper) - May be the most elegant stepper you have ever had! :large_orange_diamond:
 * [ALTextInputBar](https://github.com/AlexLittlejohn/ALTextInputBar) - An auto growing text input bar for messaging apps. :large_orange_diamond:
 * [PMZSwitch](https://github.com/kovpas/PMZSwitch) - Yet another animated toggle :large_orange_diamond:
 * [GoAutoSlideView](https://github.com/zjmdp/GoAutoSlideView) - GoAutoSlideView extends UIScrollView by featuring infinitely and automatically slide.
 * [NextGrowingTextView](https://github.com/muukii/NextGrowingTextView) - The next in the generations of 'growing textviews' optimized for iOS 7 and above.
 * [APCustomBlurView](https://github.com/collinhundley/APCustomBlurView) - A subclass of UIVisualEffectView with customizable blur radius. :large_orange_diamond:
 * [BubbleTransition](https://github.com/andreamazz/BubbleTransition) - A custom modal transition that presents and dismiss a controller with an expanding bubble effect. :large_orange_diamond:
 * [BAFluidView](https://github.com/antiguab/BAFluidView) - UIView that simulates a 2D view of a fluid in motion
 * [WZDraggableSwitchHeaderView](https://github.com/wongzigii/WZDraggableSwitchHeaderView) - :hammer: Showing status for switching between viewControllers
 * [TransitionTreasury](https://github.com/DianQK/TransitionTreasury) - Easier way to push your viewController. :large_orange_diamond:
 * [TTGTagCollectionView](https://github.com/zekunyan/TTGTagCollectionView) - Show simple text tags or custom tag views in a vertical scrollable view.
 * [MICountryPicker](https://github.com/mustafaibrahim989/MICountryPicker) - Swift country picker with search option. :large_orange_diamond:
 * [MIBadgeButton](https://github.com/mustafaibrahim989/MIBadgeButton-Swift) - Notification badge for UIButtons. :large_orange_diamond:
 * [StickyCollectionView-Swift](https://github.com/matbeich/StickyCollectionView-Swift) - UICollectionView layout for presenting of the overlapping cells. :large_orange_diamond:
 * [Switcher](https://github.com/knn90/Switcher) - Custom UISwitcher with animation :large_orange_diamond:
 * [SCNavigationControlCenter](https://github.com/SergioChan/SCNavigationControlCenter) - This is an advanced navigation control center on iOS that can allow you to navigate to whichever view controller you want
 * [SCTrelloNavigation](https://github.com/SergioChan/SCTrelloNavigation) - :clipboard: An iOS native implementation of a Trello Animated Navagation.
 * [FXBlurView](https://github.com/nicklockwood/FXBlurView) - UIView subclass that replicates the iOS 7 realtime background blur effect, but works on iOS 5 and above.
 * [NGAParallaxMotion](https://github.com/michaeljbishop/NGAParallaxMotion) - A tiny category on UIView that allows you to set one property: "parallaxIntensity" to achieve a parallax effect with UIMotionEffect
 * [EPShapes](https://github.com/ipraba/EPShapes) - Design shapes in Interface Builder. :large_orange_diamond:
 * [CRParticleEffect](https://github.com/Cleveroad/CRParticleEffect) - A CocoaPod that simplifies creation of the particle effects
 * [ValueStepper](https://github.com/BalestraPatrick/ValueStepper) - A Stepper object that displays its value. :large_orange_diamond:
 * [Spots](https://github.com/hyperoslo/Spots) - Spots is a view controller framework that makes your setup and future development blazingly fast. :large_orange_diamond:
 * [APAddressBook](https://github.com/Alterplay/APAddressBook) - Easy access to iOS address book
 * [JDSlider](https://github.com/JellyDevelopment/JDSlider) - An iOS Slider written in Swift. :large_orange_diamond:
 * [TagListView](https://github.com/xhacker/TagListView) - Simple and highly customizable iOS tag list view, in Swift. :large_orange_diamond:
 * [AZExpandableIconListView](https://github.com/Azuritul/AZExpandableIconListView) - An expandable/collapsible view component written in Swift. :large_orange_diamond:
 * [greedo-layout-for-ios](https://github.com/500px/greedo-layout-for-ios) - Full aspect ratio grid layout for iOS
 * [FlourishUI](https://github.com/thinkclay/FlourishUI) - A highly configurable and out-of-the-box-pretty UI library :large_orange_diamond:
 * [GranadaLayout](https://github.com/gskbyte/GranadaLayout) - Alternative layout system for iOS, inspired on the Android layout system, that includes linear and relative layouts, as well as an extensible JSON-based layout inflater.
 * [AMScrollingNavbar](https://github.com/andreamazz/AMScrollingNavbar) - Scrollable UINavigationBar that follows the scrolling of a UIScrollView :large_orange_diamond:
 * [Navigation Stack](https://github.com/Ramotion/navigation-stack) - Navigation Stack is a stack-modeled navigation controller. :large_orange_diamond:
 * [GMStepper](https://github.com/gmertk/GMStepper) - A stepper with a sliding label in the middle. :large_orange_diamond:
 * [UIView-draggable](https://github.com/andreamazz/UIView-draggable) - UIView category that adds dragging capabilities :large_orange_diamond:
 * [SnappingSlider](https://github.com/rehatkathuria/SnappingSlider) - A beautiful slider control for iOS built purely upon Swift :large_orange_diamond:
 * [ReplaceAnimation](https://github.com/fruitcoder/ReplaceAnimation) - UICollectionView with a sticky header flow layout, written in Swift :large_orange_diamond:
 * [PeekPop](https://github.com/marmelroy/PeekPop) - Backwards-compatible Peek and Pop.
 * [FloatRatingView](https://github.com/glenyi/FloatRatingView) - Whole, half or floating point ratings control written in Swift :large_orange_diamond:
 * [RKTagsView](https://github.com/kuler90/RKTagsView) - Highly customizable iOS tags view (like NSTokenField). Supports editing, multiple selection, Auto Layout and much more.
 * [MKGradientView](https://github.com/maxkonovalov/MKGradientView) - Core Graphics based gradient view capable of producing Linear (Axial), Radial (Circular), Conical (Angular), Bilinear (Four Point) gradients, written in Swift. 🔶
 * [EPSignature](https://github.com/ipraba/EPSignature) - Signature component for iOS in Swift :large_orange_diamond:

##### Activity Indicator

 * [NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView) - Collection of nice loading animations. :large_orange_diamond:
 * [TKRubberIndicator](https://github.com/TBXark/TKRubberIndicator) - Rubber Indicator in Swift :large_orange_diamond:
 * [RPLoadingAnimation](https://github.com/naoyashiga/RPLoadingAnimation) - Loading animations by using Swift CALayer :large_orange_diamond:
 * [LiquidLoader](https://github.com/yoavlt/LiquidLoader) - Spinner loader components with liquid animation :large_orange_diamond:
 * [iOS-CircleProgressView](https://github.com/CardinalNow/iOS-CircleProgressView) - This control will allow a user to use code instantiated or interface builder to create and render a circle progress view. :large_orange_diamond:
 * [iOS Circle Progress Bar](https://github.com/Eclair/CircleProgressBar) - iOS Circle Progress Bar
 * [LinearProgressBar](https://github.com/PhilippeBoisney/LinearProgressBar) - Linear Progress Bar (inspired by Google Material Design) for iOS written in Swift 2.0. :large_orange_diamond:
 * [STLoadingGroup](https://github.com/saitjr/STLoadingGroup) - loading views :large_orange_diamond:
 * [ALThreeCircleSpinner](https://github.com/AlexLittlejohn/ALThreeCircleSpinner) - A pulsing spinner view written in swift :large_orange_diamond:
 * [MHRadialProgressView](https://github.com/mehfuzh/MHRadialProgressView) - iOS 7 radial animated progress view.
 * [Loader](https://github.com/Ekhoo/Loader) - Amazing animated switch activity indicator written in swift
 * [MBProgressHUD](https://github.com/jdg/MBProgressHUD) - Drop-in class for displays a translucent HUD with an indicator and/or labels while work is being done in a background thread.
 * [SVProgressHUD](https://github.com/SVProgressHUD/SVProgressHUD) - A clean and lightweight progress HUD for your iOS app.
 * [ProgressHUD](https://github.com/relatedcode/ProgressHUD) - ProgressHUD is a lightweight and easy-to-use HUD.
 * [M13ProgressSuite](https://github.com/Marxon13/M13ProgressSuite) - A suite containing many tools to display progress information on iOS.
 * [JHProgressHUD](https://github.com/harikrishnant1991/JHProgressHUD) - An easy and lightweight Swift library to show HUD in IOS applications. :large_orange_diamond:
 * [PKHUD](https://github.com/pkluz/PKHUD) - A Swift based reimplementation of the Apple HUD (Volume, Ringer, Rotation,…) for iOS 8 and above. :large_orange_diamond:
 * [EZLoadingActivity](https://github.com/goktugyil/EZLoadingActivity) - Lightweight loading activity HUD.  :large_orange_diamond:
 * [FFCircularProgressView](https://github.com/elbryan/FFCircularProgressView) - FFCircularProgressView - An iOS 7-inspired blue circular progress view
 * [MRProgress](https://github.com/mrackwitz/MRProgress) - Collection of iOS drop-in components to visualize progress
 * [BigBrother](https://github.com/marcelofabri/BigBrother) - Automatically sets the network activity indicator for any performed request. :large_orange_diamond:
 * [AlamofireNetworkActivityIndicator](https://github.com/Alamofire/AlamofireNetworkActivityIndicator) - Controls the visibility of the network activity indicator on iOS using Alamofire. :large_orange_diamond:
 * [KDCircularProgress](https://github.com/kaandedeoglu/KDCircularProgress) - A circular progress view with gradients written in Swift :large_orange_diamond:
 * [DACircularProgress](https://github.com/danielamitay/DACircularProgress) - DACircularProgress is a UIView subclass with circular UIProgressView properties.
 * [KYNavigationProgress](https://github.com/ykyouhei/KYNavigationProgress) - Simple extension of UINavigationController to display progress on the UINavigationBar. :large_orange_diamond:[e]
 * [GearRefreshControl](https://github.com/andreamazz/GearRefreshControl) - A custom animation for the UIRefreshControl :large_orange_diamond:
 * [NJKWebViewProgress](https://github.com/ninjinkun/NJKWebViewProgress) - A progress interface library for UIWebView. You can implement progress bar for your in-app browser using this module.
 * [MKRingProgressView](https://github.com/maxkonovalov/MKRingProgressView) - A beautiful ring/circular progress view similar to Activity app on Apple Watch, written in Swift. 🔶

##### Alerts

 * [NZAlertView](https://github.com/NZN/NZAlertView) - Simple and intuitive alert view. Similar to push notification effect.
 * [AMSmoothAlert](https://github.com/mtonio91/AMSmoothAlert) - A cool AlertView.
 * [SweetAlert](https://github.com/codestergit/SweetAlert-iOS) - Live animated Alert View for iOS written in Swift. :large_orange_diamond:
 * [NYAlertViewController](https://github.com/nealyoung/NYAlertViewController) - Highly configurable iOS Alert Views with custom content views.
 * [SCLAlertView-Swift](https://github.com/vikmeup/SCLAlertView-Swift) - Beautiful animated Alert View, written in Swift. :large_orange_diamond:
 * [TTGSnackbar](https://github.com/zekunyan/TTGSnackbar) - Show simple message and action button on the bottom of the screen with multi kinds of animation. :large_orange_diamond:
 * [TSMessages](https://github.com/KrauseFx/TSMessages) - Show notification views on top of screen such as success, error, warning or messages for iOS.
 * [PJAlertView](https://github.com/PrajeetShrestha/PJAlertView) - Apple has deprecated beloved alert view but this library will add revamped alert view with far more customization possibility.
 * [Swift-Prompts](https://github.com/GabrielAlva/Swift-Prompts) - A Swift library to design custom prompts with a great scope of options to choose from. :large_orange_diamond:
 * [BRYXBanner](https://github.com/bryx-inc/BRYXBanner) - A lightweight dropdown notification for iOS 7+, in Swift. :large_orange_diamond:
 * [DatePickerDialog](https://github.com/squimer/DatePickerDialog-iOS-Swift) - A Swift library that displays an UIDatePicker within an UIAlertView :large_orange_diamond:
 * [LNRSimpleNotifications](https://github.com/LISNR/LNRSimpleNotifications) - Simple Swift in-app notifications. LNRSimpleNotifications is a simplified Swift port of TSMessages :large_orange_diamond:
 * [HDNotificationView](https://github.com/nhdang103/HDNotificationView) - Emulates the native Notification Banner UI for any alert.
 * [JDStatusBarNotification](https://github.com/jaydee3/JDStatusBarNotification) - Easy, customizable notifications displayed on top of the statusbar.
 * [Notie](https://github.com/thii/Notie) - In-app notification in Swift, with customizable buttons and input text field. :large_orange_diamond:
 * [EZAlertController](https://github.com/thellimist/EZAlertController) - Easy Swift UIAlertController :large_orange_diamond:
 * [SnowGlobeFramework](https://github.com/stringcode86/SnowGlobeFramework) - Delightful / slightly cheese easter egg for christmas season. Turns your awesome app into a snow globe, when user shake the device. :large_orange_diamond:
 * [GSMessages](https://github.com/wxxsw/GSMessages) - A simple style messages/notifications for iOS 7+. :large_orange_diamond:
 * [OEANotification](https://github.com/OEASLAN/OEANotification) - In-app customizable notification views on top of screen for iOS which is written in Swift 2.1. :large_orange_diamond:
 * [GSAlert](https://github.com/wxxsw/GSAlert) - If you want to use UIAlertController, but still need to support iOS 7 this project is for you. :large_orange_diamond:
 * [CZPicker](https://github.com/chenzeyu/CZPicker) - A picker view shown as a popup for iOS.
 * [RKDropdownAlert](https://github.com/cwRichardKim/RKDropdownAlert) - Extremely simple UIAlertView alternative.
 * [TKSwarmAlert](https://github.com/entotsu/TKSwarmAlert) - Animated alert library like Swarm app. :large_orange_diamond:
 * [Whisper](https://github.com/hyperoslo/Whisper) - Whisper is a component that will make the task of display messages and in-app notifications simple. It has three different views inside :large_orange_diamond:
 * [SimpleAlert](https://github.com/KyoheiG3/SimpleAlert) - Customizable simple Alert and simple ActionSheet for Swift :large_orange_diamond:
 * [Hokusai](https://github.com/ytakzk/Hokusai) - A Swift library to provide a bouncy action sheet :large_orange_diamond:
 * [SwiftNotice](https://github.com/johnlui/SwiftNotice) - SwiftNotice is a GUI library for displaying various popups (HUD) written in pure Swift, fits any scrollview. :large_orange_diamond:
 * [SwiftOverlays](https://github.com/peterprokop/SwiftOverlays) - SwiftOverlays is a Swift GUI library for displaying various popups and notifications :large_orange_diamond:
 * [SwiftyDrop](https://github.com/morizotter/SwiftyDrop) - SwiftyDrop is a lightweight pure Swift simple and beautiful dropdown message. :large_orange_diamond:
 * [LKAlertController](https://github.com/Lightningkite/LKAlertController) - An easy to use UIAlertController builder for swift. :large_orange_diamond:

##### Calendar
 * [CVCalendar](https://github.com/Mozharovsky/CVCalendar) - A custom visual calendar for iOS 8+ written in Swift (2.0). :large_orange_diamond:
 * [RSDayFlow](https://github.com/ruslanskorb/RSDayFlow) - iOS 7+ Calendar with Infinite Scrolling.
 * [NWCalendarView](https://github.com/nbwar/NWCalendarView) - An availability calendar implementation for iOS :large_orange_diamond:
 * [FSCalendar](https://github.com/WenchaoD/FSCalendar) - A superiorly awesome iOS7+ calendar control, compatible with both Objective-c and Swift2 https://www.cocoacontrols.com/controls/fscalendar :large_orange_diamond:
 * [GLCalendarView](https://github.com/Glow-Inc/GLCalendarView) - A fully customizable calendar view acting as a date range picker
 * [JTCalendar](https://github.com/jonathantribouharet/JTCalendar) - A customizable calendar view for iOS.

##### Form
 * [Form](https://github.com/hyperoslo/Form) - The most flexible and powerful way to build a form on iOS
 * [XLForm](https://github.com/xmartlabs/XLForm) - XLForm is the most flexible and powerful iOS library to create dynamic table-view forms. Fully compatible with Swift & Obj-C.
 * [Eureka](https://github.com/xmartlabs/Eureka) - Elegant iOS form builder in pure Swift. :large_orange_diamond:
 * [YALField](https://github.com/Yalantis/YALField) - Custom Field component with validation for creating easier form-like UI from interface builder.
 * [Former](https://github.com/ra1028/Former) - Former is a fully customizable Swift2 library for easy creating UITableView based form. :large_orange_diamond:
 * [SwiftForms](https://github.com/ortuman/SwiftForms) - A small and lightweight library written in Swift that allows you to easily create forms. :large_orange_diamond:

##### Table View
 * [MGSwipeTableCell](https://github.com/MortimerGoro/MGSwipeTableCell) - UITableViewCell subclass that allows to display swippable buttons with a variety of transitions.
 * [ParallaxTableViewHeader](https://github.com/Vinodh-G/ParallaxTableViewHeader) - Parallax scrolling effect on UITableView header view when a tableView is scrolled.
 * [YXTPageView](https://github.com/hanton/YXTPageView) - A PageView, which supporting scrolling to transition between a UIView and a UITableView.
 * [DZNEmptyDataSet](https://github.com/dzenbot/DZNEmptyDataSet) - A drop-in UITableView/UICollectionView superclass category for showing empty datasets whenever the view has no content to display.
 * [ConfigurableTableViewController](https://github.com/fastred/ConfigurableTableViewController) - Typed, yet Flexible Table View Controller http://holko.pl/2016/01/05/typed-table-view-controller/ :large_orange_diamond:
 * [CSStickyHeaderFlowLayout](https://github.com/jamztang/CSStickyHeaderFlowLayout) - UICollectionView replacement of UITableView. Do even more like Parallax Header, Sticky Section Header. :large_orange_diamond:
 * [folding-cell](https://github.com/Ramotion/folding-cell) - TableViewCell replacement with parallax detail view for Swift :large_orange_diamond:
 * [Lightning-Table](https://github.com/electrickangaroo/Lightning-Table) - A declarative api for working with UITableView.
 * [Static](https://github.com/venmo/Static) - Simple static table views for iOS in Swift. :large_orange_diamond:
 * [GSKStretchyHeaderView](https://github.com/gskbyte/GSKStretchyHeaderView) - Configurable yet easy to use stretchy header view for UITableView and UICollectionView.
 * [MEVFloatingButton](https://github.com/manuelescrig/MEVFloatingButton) - An iOS drop-in UITableView, UICollectionView and UIScrollView superclass category for showing a customizable floating button on top of it.
 * [AMWaveTransition](https://github.com/andreamazz/AMWaveTransition) - Custom transition between viewcontrollers holding tableviews :large_orange_diamond:
 * [Dwifft](https://github.com/jflinter/Dwifft) - Automatic updates of UITableView with animations in Swift :large_orange_diamond:

##### TextField & TextView

 * [JVFloatLabeledTextField](https://github.com/jverdi/JVFloatLabeledTextField) - UITextField subclass with floating labels.
 * [ARAutocompleteTextView](https://github.com/alexruperez/ARAutocompleteTextView) - subclass of UITextView that automatically displays text suggestions in real-time. Perfect for email Textviews.
 * [IQDropDownTextField](https://github.com/hackiftekhar/IQDropDownTextField) - TextField with DropDown support using UIPickerView
 * [UITextField-Shake](https://github.com/andreamazz/UITextField-Shake) - UITextField category that adds shake animation. [Also with Swift version](https://github.com/King-Wizard/UITextField-Shake-Swift) :large_orange_diamond:
 * [HTYTextField](https://github.com/hanton/HTYTextField) - A UITextField with bouncy placeholder. :large_orange_diamond:
 * [MVAutocompletePlaceSearchTextField](https://github.com/mrugrajsinh/MVAutocompletePlaceSearchTextField) - A drop-in Autocompletion control for Place Search like Google Places, Uber, etc.
 * [AutocompleteField](https://github.com/filipstefansson/AutocompleteField) - Add word completion to your UITextFields. :large_orange_diamond:
 * [RSKGrowingTextView](https://github.com/ruslanskorb/RSKGrowingTextView) - A light-weight UITextView subclass that automatically grows and shrinks. :large_orange_diamond:
 * [RSKPlaceholderTextView](https://github.com/ruslanskorb/RSKPlaceholderTextView) - A light-weight UITextView subclass that adds support for placeholder. :large_orange_diamond:
 * [StatefulViewController](https://github.com/aschuch/StatefulViewController) - Placeholder views based on content, loading, error or empty states :large_orange_diamond:
 * [SlackTextViewController](https://github.com/slackhq/SlackTextViewController) - A drop-in UIViewController subclass with a growing text input view and other useful messaging features.
 * [MBAutoGrowingTextView](https://github.com/MatejBalantic/MBAutoGrowingTextView) - An auto-layout base UITextView subclass which automatically grows with user input and can be constrained by maximal and minimal height - all without a single line of code
 * [TextFieldEffects](https://github.com/raulriera/TextFieldEffects) - Custom UITextFields effects inspired by Codrops, built using Swift :large_orange_diamond:
 * [Reel Search](https://github.com/Ramotion/reel-search) - RAMReel is a controller that allows you to choose options from a list. :large_orange_diamond:
  * [MLPAutoCompleteTextField](https://github.com/EddyBorja/MLPAutoCompleteTextField) - a subclass of UITextField that behaves like a typical UITextField with one notable exception: it manages a drop down table of autocomplete suggestions that update as the user types.

##### Keyboard
 * [RSKKeyboardAnimationObserver](https://github.com/ruslanskorb/RSKKeyboardAnimationObserver) - Showing / dismissing keyboard animation in simple UIViewController category.
 * [RFKeyboardToolbar](https://github.com/ruddfawcett/RFKeyboardToolbar) - This is a flexible UIView and UIButton subclass to add customized buttons and toolbars to your UITextFields/UITextViews.
 * [IQKeyboardManager](https://github.com/hackiftekhar/IQKeyboardManager) - Codeless drop-in universal library allows to prevent issues of keyboard sliding up and cover UITextField/UITextView.
 * [NgKeyboardTracker](https://github.com/meiwin/NgKeyboardTracker) - Objective-C library for tracking keyboard in iOS apps.
 * [MMNumberKeyboard](https://github.com/matmartinez/MMNumberKeyboard) - A simple keyboard to use with numbers and, optionally, a decimal point.
 * [KeyboardObserver](https://github.com/morizotter/KeyboardObserver) - For less complicated keyboard event handling. :large_orange_diamond:
 * [TPKeyboardAvoiding](https://github.com/michaeltyson/TPKeyboardAvoiding) - A drop-in universal solution for moving text fields out of the way of the keyboard in iOS
 * [YYKeyboardManager](https://github.com/ibireme/YYKeyboardManager) - iOS utility class allows you to access keyboard view and track keyboard animation.
 * [KeyboardMan](https://github.com/nixzhu/KeyboardMan) - KeyboardMan helps you make keyboard animation. :large_orange_diamond:

##### Button
 * [SSBouncyButton](https://github.com/StyleShare/SSBouncyButton) - iOS7-style bouncy button UI component.
 * [DOFavoriteButton](https://github.com/okmr-d/DOFavoriteButton) - Cute Animated Button written in Swift. :large_orange_diamond:
 * [SDevBootstrapButton](https://github.com/0x73/SDevBootstrapButton) - Twitter Bootstrap buttons for Swift :large_orange_diamond:
 * [SDevCircleButton](https://github.com/0x73/SDevCircleButton) - Circle Button for Swift :large_orange_diamond:
 * [VBFPopFlatButton](https://github.com/victorBaro/VBFPopFlatButton) - Flat button with 9 different states animated using Facebook POP.
 * [HTPressableButton](https://github.com/herinkc/HTPressableButton) - Flat design pressable button.
 * [LiquidFloatingActionButton](https://github.com/yoavlt/LiquidFloatingActionButton) - Material Design Floating Action Button in liquid state
 * [JTFadingInfoView](https://github.com/JunichiT/JTFadingInfoView) - An UIButton-based view with fade in/out animation features.
 * [KCFloatingActionButton](https://github.com/kciter/KCFloatingActionButton) - Simple Floating Action Button for iOS :large_orange_diamond:
 * [Hamburger-Menu-Button](https://github.com/toannt/Hamburger-Menu-Button) - A hamburger menu button with full customization. :large_orange_diamond:
 * [TVButton](https://github.com/marmelroy/TVButton) - Recreating the cool parallax icons from Apple TV as iOS UIButtons (in Swift). :large_orange_diamond:
 * [SwiftyButton](https://github.com/TakeScoop/SwiftyButton) - Simple and customizable button in Swift :large_orange_diamond:
 * [AnimatablePlayButton](https://github.com/suzuki-0000/AnimatablePlayButton) - Animated Play and Pause Button using CALayer, CAKeyframeAnimation. :large_orange_diamond:
 * [VCFloatingActionButton](https://github.com/gizmoboy7/VCFloatingActionButton) - A Floating Action Button just like Google inbox for iOS
 * [FlowBarButtonItem](https://github.com/noppefoxwolf/FlowBarButtonItem) - Bar Button Item that can be moved anywhere in the screen, like Android's stickers button. :large_orange_diamond:
 * [gbkui-button-progress-view](https://github.com/Guidebook/gbkui-button-progress-view) - UIButton Inspired by Apple’s download progress buttons in the app store
 * [ZFRippleButton](https://github.com/zoonooz/ZFRippleButton) - Custom UIButton effect inspired by Google Material Design :large_orange_diamond:

##### Menu
 * [ENSwiftSideMenu](https://github.com/evnaz/ENSwiftSideMenu) - A simple side menu for iOS 7/8 written in Swift. :large_orange_diamond:
 * [RESideMenu](https://github.com/romaonthego/RESideMenu) - iOS 7/8 style side menu with parallax effect inspired by Dribbble shots.
 * [SSASideMenu](https://github.com/SSA111/SSASideMenu) - A Swift implementation of RESideMenu. A iOS 7/8 style side menu with parallax effect. :large_orange_diamond:
 * [PagingMenuController](https://github.com/kitasuke/PagingMenuController) - Paging view controller with customizable menu in Swift. :large_orange_diamond:
 * [RadialMenu](https://github.com/bradjasper/radialmenu) - RadialMenu is a custom control for providing a touch context menu (like iMessage recording in iOS 8) built with Swift & POP :large_orange_diamond:
 * [cariocamenu](https://github.com/arn00s/cariocamenu) - The fastest zero-tap iOS menu. :large_orange_diamond:
 * [VLDContextSheet](https://github.com/vangelov/VLDContextSheet) - Context menu similar to the one in the Pinterest iOS app
 * [GuillotineMenu](https://github.com/Yalantis/GuillotineMenu) - Guillotine (Drop down) transitioning animation menu :large_orange_diamond:
 * [MediumMenu](https://github.com/pixyzehn/MediumMenu) - A menu based on Medium iOS app. :large_orange_diamond:
 * [SwiftySideMenu](https://github.com/hossamghareeb/SwiftySideMenu) - a lightweight, fully customizable side menu for iOS inspired from [TimeLine app](https://itunes.apple.com/us/app/timeline-news-in-context/id948867534?mt=8&ign-mpt=uo%3D4). Built with spring animations using Facebook Pop.
 * [LLSlideMenu](https://github.com/lilei644/LLSlideMenu) - This is a spring slide menu for iOS apps
 * [Swift-Slide-Menu](https://github.com/PhilippeBoisney/Swift-Slide-Menu) - A Slide Menu, written in Swift, inspired by Slide Menu Material Design. :large_orange_diamond:
 * [MenuItemKit](https://github.com/cxa/MenuItemKit) - UIMenuItem with image and block(closure) :large_orange_diamond:
 * [BTNavigationDropdownMenu](https://github.com/PhamBaTho/BTNavigationDropdownMenu) - The elegant dropdown menu, written in Swift, appears underneath navigation bar to display a list of related items when a user click on the navigation title. :large_orange_diamond:
 * [ALRadialMenu](https://github.com/AlexLittlejohn/ALRadialMenu) - A radial/circular menu featuring spring animations. Written in swift :large_orange_diamond:
 * [AZDropdownMenu](https://github.com/Azuritul/AZDropdownMenu) - An easy to use dropdown menu that supports images. :large_orange_diamond:
 * [CircleMenu](https://github.com/Ramotion/circle-menu) - An animated, multi-option menu button. :large_orange_diamond:
 * [SlideMenuControllerSwift](https://github.com/dekatotoro/SlideMenuControllerSwift) - iOS Slide Menu View based on Google+, iQON, Feedly, Ameba iOS app. It is written in pure Swift. :large_orange_diamond:
 * [SideMenu](https://github.com/jonkykong/SideMenu) - Simple side menu control in Swift inspired by Facebook. Right and Left sides. Lots of customization and animation options. Can be implemented in Storyboard with no code. :large_orange_diamond:
 * [CategorySliderView](https://github.com/cemolcay/CategorySliderView) - slider view for choosing categories. add any UIView type as category item view. Fully customisable
 * [MKDropdownMenu](https://github.com/maxkonovalov/MKDropdownMenu) - A Dropdown Menu for iOS with many customizable parameters to suit any needs.

##### Label
 * [LTMorphingLabel](https://github.com/lexrus/LTMorphingLabel) - Graceful morphing effects for UILabel written in Swift. :large_orange_diamond:
 * [ActiveLabel.swift](https://github.com/optonaut/ActiveLabel.swift) - UILabel drop-in replacement supporting Hashtags (#), Mentions (@) and URLs (http://) :large_orange_diamond:
 * [MZTimerLabel](https://github.com/mineschan/MZTimerLabel) - A handy class for iOS to use UILabel as a countdown timer or stopwatch just like in Apple Clock App.
 * [CountdownLabel](https://github.com/suzuki-0000/CountdownLabel) - Simple countdown UILabel with morphing animation, and some useful function. :large_orange_diamond:
 * [IncrementableLabel](https://github.com/recisio/IncrementableLabel) - Incrementable label for iOS, OS X, and tvOS. :large_orange_diamond:
 * [TTTAttributedLabel](https://github.com/TTTAttributedLabel/TTTAttributedLabel) - A drop-in replacement for UILabel that supports attributes, data detectors, links, and more

##### Popup
 * [KLCPopup](https://github.com/jmascia/KLCPopup) - A simple and flexible class for presenting custom views as a popup in iOS.
 * [MMPopupView](https://github.com/adad184/MMPopupView) - Pop-up based view(e.g. alert sheet), can easily customize.
 * [STPopup](https://github.com/kevin0571/STPopup) - STPopup provides a UINavigationController in popup style, for both iPhone and iPad.
 * [NMPopUpView](https://github.com/psy2k/NMPopUpView) - Simple iOS class for showing nice popup windows. Swift and Objective-C versions available. :large_orange_diamond:
 * [CNPPopupController](https://github.com/carsonperrotti/CNPPopupController) - Simple and versatile class for presenting a custom popup in a variety of fashions. It includes a many options for controlling how your popup appears and behaves.

##### Pull to Refresh
 * [DGElasticPullToRefresh](https://github.com/gontovnik/DGElasticPullToRefresh) - Elastic pull to refresh for iOS developed in Swift :large_orange_diamond:
 * [PullToBounce](https://github.com/entotsu/PullToBounce) - Animated "Pull To Refresh" Library for UIScrollView. :large_orange_diamond:
 * [SVPullToRefresh](https://github.com/samvermette/SVPullToRefresh) - Give pull-to-refresh & infinite scrolling to any UIScrollView with 1 line of code. http://samvermette.com/314
 * [UzysAnimatedGifPullToRefresh](https://github.com/uzysjung/UzysAnimatedGifPullToRefresh) - Add PullToRefresh using animated GIF to any scrollView with just simple code
 * [PullToRefreshCoreText](https://github.com/cemolcay/PullToRefreshCoreText) - PullToRefresh extension for all UIScrollView type classes with animated text drawing style
 * [BOZPongRefreshControl](https://github.com/boztalay/BOZPongRefreshControl) - A pull-down-to-refresh control for iOS that plays pong, originally created for the MHacks III iOS app
 * [CBStoreHouseRefreshControl](https://github.com/coolbeet/CBStoreHouseRefreshControl) - Fully customizable pull-to-refresh control inspired by Storehouse iOS app :large_orange_diamond:
 * [mntpulltoreact](https://github.com/mentionapp/mntpulltoreact) - One gesture, many actions. An evolution of Pull to Refresh.

##### Slider
 * [VolumeControl](https://github.com/12Rockets/VolumeControl) - Custom volume control for iPhone featuring a well-designed round slider.
 * [WESlider](https://github.com/Ekhoo/WESlider) - Simple and light weight slider with chapter management
 * [IntervalSlider](https://github.com/shushutochako/IntervalSlider) - IntervalSlider is a slider library like ReutersTV app. written in pure swift. :large_orange_diamond:
 * [RangeSlider](https://github.com/warchimede/RangeSlider) - A simple range slider made in Swift :large_orange_diamond:
 * [CircleSlider](https://github.com/shushutochako/CircleSlider) - CircleSlider is a Circular slider library. written in pure Swift. :large_orange_diamond:
 * [MARKRangeSlider](https://github.com/vadymmarkov/MARKRangeSlider) - A custom reusable slider control with 2 thumbs (range slider).
 * [ASValueTrackingSlider](https://github.com/alskipp/ASValueTrackingSlider) - A UISlider subclass that displays the slider value in a popup view
 * [TTRangeSlider](https://github.com/TomThorpe/TTRangeSlider) - A slider, similar in style to UISlider, but which allows you to pick a minimum and maximum range.

##### Tab Bar
 * [ESTabBarController](https://github.com/ezescaruli/ESTabBarController) - A tab bar controller for iOS that allows highlighting buttons and setting custom actions to them.
 * [GooeyTabbar](https://github.com/KittenYang/GooeyTabbar) -A gooey effect tabbar :large_orange_diamond:
 * [animated-tab-bar](https://github.com/Ramotion/animated-tab-bar) - RAMAnimatedTabBarController is a Swift module for adding animation to tabbar items. :large_orange_diamond:
 * [FoldingTabBar.iOS](https://github.com/Yalantis/FoldingTabBar.iOS) - Folding Tab Bar and Tab Bar Controller
 * [GGTabBar](https://github.com/Goles/GGTabBar) - Another UITabBar & UITabBarController (iOS Tab Bar) replacement, but uses Auto Layout for arranging it's views hierarchy.
 * [adaptive-tab-bar](https://github.com/Ramotion/adaptive-tab-bar) - AdaptiveController is a 'Progressive Reduction' Swift module for adding custom states to Native or Custom iOS UI elements
 * [Pager](https://github.com/lucoceano/Pager) - Easily create sliding tabs with Pager :large_orange_diamond:
 * [XLPagerTabStrip](https://github.com/xmartlabs/XLPagerTabStrip) - Android PagerTabStrip for iOS. :large_orange_diamond:

### WebSocket
 * [SocketRocket](https://github.com/square/SocketRocket) - A conforming Objective-C WebSocket client library.
 * [socket.io-client-swift](https://github.com/socketio/socket.io-client-swift) - Socket.IO-client for iOS/OS X. :large_orange_diamond:
 * [SwiftWebSocket](https://github.com/tidwall/SwiftWebSocket) - High performance WebSocket client library for Swift, iOS and OSX. :large_orange_diamond:
 * [Starscream](https://github.com/daltoniam/Starscream) - Websockets in swift for iOS and OSX :large_orange_diamond:
 * [SwiftSocket](https://github.com/swiftsocket/SwiftSocket) - simple socket library for apple swift lang. :large_orange_diamond:

### Code Quality
 * [KZBootstrap](https://github.com/krzysztofzablocki/KZBootstrap) - iOS project bootstrap aimed at high quality coding.
 * [KZAsserts](https://github.com/krzysztofzablocki/KZAsserts) - Set of custom assertions that automatically generate NSError's, allow for both Assertions in Debug and Error handling in Release builds, with beautiful DSL.
 * [PSPDFUIKitMainThreadGuard](https://gist.github.com/steipete/5664345) - Simple snippet generating assertions when UIKit is used on background threads.
 * [Flex](https://github.com/Flipboard/FLEX) - An in-app debugging and exploration tool for iOS.
 * [chisel](https://github.com/facebook/chisel) - Collection of LLDB commands to assist debugging iOS apps.
 * [OCLint](http://oclint.org/) - Static code analysis tool for improving quality and reducing defects.
 * [ocstyle](https://github.com/Cue/ocstyle) - Objective-C style checker.
 * [SwiftLint](https://github.com/realm/SwiftLint) - An experimental tool to enforce Swift style and conventions. :large_orange_diamond:
 * [spacecommander](https://github.com/square/spacecommander) - Commit fully-formatted Objective-C code as a team without even trying.
 * [DWURecyclingAlert](https://github.com/diwu/DWURecyclingAlert) - Optimizing UITableViewCell For Fast Scrolling.
 * [DCIntrospect](https://github.com/domesticcatsoftware/DCIntrospect) - Small library of visual debugging tools for iOS.
 * [Tailor](https://github.com/sleekbyte/tailor) - Cross-platform static analyzer for Swift that helps you to write cleaner code and avoid bugs.
 * [SwiftCop](https://github.com/andresinaka/SwiftCop) -  SwiftCop is a validation library fully written in Swift and inspired by the clarity of Ruby On Rails Active Record validations. :large_orange_diamond:
 * [Trackable](https://github.com/VojtaStavik/Trackable) - Trackable is a simple analytics integration helper library. It’s especially designed for easy and comfortable integration with existing projects. :large_orange_diamond:
 * [MLeaksFinder](https://github.com/Zepo/MLeaksFinder) - Find memory leaks in your iOS app at develop time.
 * [HeapInspector-for-iOS](https://github.com/tapwork/HeapInspector-for-iOS) - Find memory issues & leaks in your iOS app without instruments

### Analytics
 * [Mixpanel](https://mixpanel.com/) - Advanced analytics platform.
 * [Localytics](https://www.localytics.com/) - Brings app marketing and analytics together.
 * [Answers by Fabric](https://answers.io/) - Answers gives you real-time insight into people’s experience in your app.
 * [Liquid Analytics](https://onliquid.com) - Identify behaviours through Analytics and react with real-time Personalization.
 * [GTrack](https://github.com/gemr/GTrack) - Lightweight Objective-C wrapper around the Google Analytics for iOS SDK with some extra goodies.
 * [ARAnalytics](https://github.com/orta/ARAnalytics) - Analytics abstraction library offering a sane API for tracking events and user data.
 * [Segment](https://github.com/segmentio/analytics-ios) - The hassle-free way to integrate analytics into any iOS application.
 * [MOCA Analytics](https://mocaplatform.com/features) - Paid cross-platform analytics backend.
 * [Countly](https://count.ly) - Open source, mobile & web analytics, crash reports and push notifications platform for iOS & Android.
 * [Abbi](https://github.com/abbiio/iosdk) - A Simple SDK for developers to manage and maximise conversions of all in-app promotions.

### Payments
 * [Stripe](https://stripe.com) - Payment integration on your app with PAY. Suitable for people with low knowlege on Backend.
 * [Braintree](https://www.braintreepayments.com) - Free payment processing on your first $50k. Requires Backend.
 * [Venmo](https://github.com/venmo/venmo-ios-sdk) Make and accept payments in your iOS app via Venmo.
 * [Moltin](https://moltin.com/ios-ecommerce-sdk) - Add eCommerce to your app with a simple SDK, so you can create a store and sell physical products, no backend required.
 * [PatronKit](https://github.com/MosheBerman/PatronKit) - A framework to add patronage to your apps. :large_orange_diamond:
 * [SwiftyStoreKit](https://github.com/bizz84/SwiftyStoreKit) - Lightweight In App Purchases Swift framework for iOS 8.0+ and OSX 9.0+ :large_orange_diamond:
 * [InAppFramework](https://github.com/sandorgyulai/InAppFramework) - In App Purchase Manager framework for iOS :large_orange_diamond:
 * [SwiftInAppPurchase](https://github.com/rpzzzzzz/SwiftInAppPurchase) - Simply code In App Purchases with this Swift Framework :large_orange_diamond:

### Products
 * [Import.io](https://www.import.io/) - Instantly Turn Web Pages into Data.
 * [Tapglue](https://www.tapglue.com) - Build social products and a activity feed with a few lines of code.

### Utility
  * [Underscore.m](https://github.com/robb/Underscore.m) - A DSL for Data Manipulation.
  * [SBConstants](https://github.com/paulsamuels/SBConstants) - Generate a constants file by grabbing identifiers from storyboards in a project.
  * [XExtensionItem](https://github.com/tumblr/XExtensionItem) - Easier sharing of structured data between iOS applications and share extensions.
  * [ReflectableEnum](https://github.com/fastred/ReflectableEnum) - Reflection for enumerations in Objective-C.
  * [EKAlgorithms](https://github.com/EvgenyKarkan/EKAlgorithms) - Some well known CS algorithms & data structures in Objective-C.
  * [Tactile](https://github.com/delba/Tactile) - The Swift way to add UIGestureRecognizer and to react to UIControlEvents :large_orange_diamond:
  * [ObjectiveSugar](https://github.com/supermarin/ObjectiveSugar) - ObjectiveC additions for humans. Ruby style.
  * [GroundControl](https://github.com/mattt/GroundControl) - Remote configuration for iOS.
  * [OpinionatedC](https://github.com/leoschweizer/OpinionatedC) - Because Objective-C should have inherited more from Smalltalk.
  * [SwiftRandom](https://github.com/thellimist/SwiftRandom) - Generator for random data. :large_orange_diamond:
  * [RandomKit](https://github.com/nvzqz/RandomKit/) - Random data generation in Swift. :large_orange_diamond:
  * [YOLOKit](https://github.com/mxcl/YOLOKit) - Getting square objects down round holes.
  * [EZSwiftExtensions](https://github.com/goktugyil/EZSwiftExtensions) - :smirk: How Swift standard types and classes were supposed to work. :large_orange_diamond:[e]
  * [Pantry](https://github.com/nickoneill/Pantry) - The missing light persistence layer for Swift :large_orange_diamond:
  * [SwiftParsec](https://github.com/davedufresne/SwiftParsec) - A parser combinator library written in the Swift programming language. :large_orange_diamond:
  * [OrderedSet](https://github.com/Weebly/OrderedSet) - A Swift collection of unique, ordered objects :large_orange_diamond:
  * [Datez](https://github.com/SwiftKitz/Datez) - Swift library for dealing with `NSDate`, `NSCalendar`, and `NSDateComponents`. :large_orange_diamond:
  * [BFKit](https://github.com/FabrizioBrancati/BFKit) - An Objective-C collection of useful classes to develop Apps faster.
  * [BFKit-Swift](https://github.com/FabrizioBrancati/BFKit-Swift) - A Swift collection of useful classes to develop Apps faster. :large_orange_diamond:
  * [Scale](https://github.com/onmyway133/scale) - Unit converter in Swift (available via CocoaPods) :large_orange_diamond:
  * [Standard Template Protocols](https://github.com/cconeil/Standard-Template-Protocols) - Protocols for your every day iOS needs :large_orange_diamond:
  * [TimeLord](https://github.com/JonFir/TimeLord) - Easy DateTime (`NSDate`, `NSCalendar`, `NSDateComponents`, `NSDateFormatter`) management :large_orange_diamond:
  * [AppVersionMonitor](https://github.com/eure/AppVersionMonitor) - Monitor iOS app version easily.
  * [Sugar](https://github.com/hyperoslo/Sugar) - Something sweet that goes great with your Cocoa. :large_orange_diamond:[e]
  * [Then](https://github.com/devxoul/Then) - ✨ Super sweet syntactic sugar for Swift initializers. :large_orange_diamond:[e]
  * [Kvitto](https://github.com/Cocoanetics/Kvitto) - App Store Receipt Validation :large_orange_diamond:
  * [Reusable](https://github.com/AliSoftware/Reusable) - A Swift mixin for UITableViewCells and UICollectionViewCells :large_orange_diamond:
  * [Notificationz](https://github.com/SwiftKitz/Notificationz) - Helping you own NSNotificationCenter in Swift :large_orange_diamond:
  * [SwiftFoundation](https://github.com/PureSwift/SwiftFoundation) - Cross-Platform, Protocol-Oriented Programming base library to complement the Swift Standard Library. (Pure Swift, Supports Linux) :large_orange_diamond:[e]
  * [libextobjc](https://github.com/jspahrsummers/libextobjc) - A Cocoa library to extend the Objective-C programming language.
  * [VersionTrackerSwift](https://github.com/tbaranes/VersionTrackerSwift) - Track which versions of your app a user has previously installed. :large_orange_diamond:
  * [DeviceGuru](https://github.com/InderKumarRathore/DeviceGuru/) - DeviceGuru is a simple lib (Swift) to know the exact type of the device, e.g. iPhone 6 or iPhone 6s. :large_orange_diamond:

#### GCD
  * [GCDKit](https://github.com/JohnEstropia/GCDKit) - Grand Central Dispatch simplified with Swift. :large_orange_diamond:
  * [Async](https://github.com/duemunk/Async) - Syntactic sugar in Swift for asynchronous dispatches in Grand Central Dispatch :large_orange_diamond:
  * [SwiftSafe](https://github.com/czechboy0/SwiftSafe) - Thread synchronization made easy :large_orange_diamond:
  * [YYDispatchQueuePool](https://github.com/ibireme/YYDispatchQueuePool) - iOS utility class to manage global dispatch queue.
  * [AlecrimAsyncKit](https://github.com/Alecrim/AlecrimAsyncKit) - Bringing async and await to Swift world with some flavouring. :large_orange_diamond:

# Project setup
 * [crafter](https://github.com/krzysztofzablocki/crafter) - CLI that allows you to configure iOS project's template using custom DSL syntax, simple to use and quite powerful.
 * [liftoff](https://github.com/thoughtbot/liftoff) - Another CLI for creating iOS projects.
 * [amaro](https://github.com/crushlovely/Amaro) - iOS Boilerplate full of delights.
 * [chairs](https://github.com/orta/chairs) - Swap around your iOS Simulator Documents

# Server
 * [Perfect](https://github.com/PerfectlySoft/Perfect) - Server-side Swift. The Perfect library, application server, connectors and example apps. :large_orange_diamond:
 * [Swifter](https://github.com/httpswift/swifter) - Tiny http server engine written in Swift programming language. :large_orange_diamond:
 * [CocoaHTTPServer](https://github.com/robbiehanson/CocoaHTTPServer) - A small, lightweight, embeddable HTTP server for Mac OS X or iOS applications.
 * [Curassow](https://github.com/kylef/Curassow) - Swift HTTP server using the pre-fork worker model. :large_orange_diamond:
 * [Zewo](https://github.com/Zewo/Zewo) - Venice based HTTP server for Swift 2.2 on Linux :large_orange_diamond:
 * [Vapor](https://github.com/qutheory/vapor) - Elegant web framework for Swift that works on iOS, OS X, and Ubuntu. :large_orange_diamond:
 * [swiftra](https://github.com/takebayashi/swiftra) - Sinatra-like DSL for developing web apps in Swift :large_orange_diamond:
 * [blackfish](https://github.com/elliottminns/blackfish) - A fast HTTP web server based on Node.js and Express written in Swift :large_orange_diamond:
 * [swift-http](https://github.com/huytd/swift-http) - HTTP Implementation for Swift on Linux and Mac OS X :large_orange_diamond:
 * [Trevi](https://github.com/Yoseob/Trevi) - A powerful Swift Web Application Server Framework Project :large_orange_diamond:
 * [Express](https://github.com/crossroadlabs/Express) - Swift Express is a simple, yet unopinionated web application server written in Swift :large_orange_diamond:
 * [Aeon](https://github.com/Zewo/Aeon) - Aeon is a GCD based HTTP server for Swift 2. :large_orange_diamond:
 * [Taylor](https://github.com/izqui/Taylor) - A lightweight library for writing HTTP web servers with Swift :large_orange_diamond:
 * [Frank](https://github.com/nestproject/Frank) - Frank is a DSL for quickly writing web applications in Swift
 * [Kitura](https://github.com/IBM-Swift/Kitura) - Web framework and HTTP server for Swift by IBM :large_orange_diamond:
 * [Swifton](https://github.com/necolt/Swifton) - A Ruby on Rails inspired Web Framework for Swift that runs on Linux and OS X :large_orange_diamond:
 * [Dynamo](https://github.com/johnno1962/Dynamo) - High Performance (nearly)100% Swift Web server supporting dynamic content. :large_orange_diamond:

# Dependency / Package Manager
 * [CocoaPods](https://cocoapods.org/) - CocoaPods is the dependency manager for Objective-C projects. It has thousands of libraries and can help you scale your projects elegantly.
 * [Xcode Maven](http://sap-production.github.io/xcode-maven-plugin/site/) - The Xcode Maven Plugin can be used in order to run Xcode builds embedded in a Maven lifecycle.
 * [Gradle](http://openbakery.org/gradle.html) - The gradle xcode plugin can be used to build iOS or Mac OS X Projects using gradle.
 * [Carthage](https://github.com/Carthage/Carthage) - A simple, decentralized dependency manager for Cocoa. :large_orange_diamond:
 * [SWM (Swift Modules)](https://github.com/jankuca/swm) - A package/dependency manager for Swift projects similar to npm (node.js package manager) or bower (browser package manager from Twitter). Does not require the use of XCode. :large_orange_diamond:
 * [Alcatraz](http://alcatraz.io/) - The package manager for Xcode.
 * [CocoaSeeds](https://github.com/devxoul/CocoaSeeds) - Git Submodule Alternative for Cocoa.
 * [Podage](https://github.com/jensmeder/Podage) - A simple tool to bundle any Cocoapod and its dependencies into frameworks.
 * [swift-package-manager](https://github.com/apple/swift-package-manager) - The Package Manager for the Swift Programming Language, by Apple :large_orange_diamond:

# Testing

### TDD / BDD
 * [Kiwi](https://github.com/kiwi-bdd/Kiwi) - A behavior-driven development library for iOS development.
 * [Specta](https://github.com/specta/specta) - A light-weight TDD / BDD framework for Objective-C & Cocoa.
 * [Quick](https://github.com/Quick/Quick) - A behavior-driven development framework for Swift and Objective-C.
 * [XcodeCoverage](https://github.com/jonreid/XcodeCoverage) - Code coverage for Xcode projects.
 * [OHHTTPStubs](https://github.com/AliSoftware/OHHTTPStubs) - Stub your network requests easily! Test your apps with fake network data and custom response time, response code and headers!
 * [Dixie](https://github.com/Skyscanner/Dixie) - Dixie is an open source Objective-C testing framework for altering object behaviours.
 * [gh-unit](https://github.com/gh-unit/gh-unit) - Test Framework for Objective-C.
 * [Nimble](https://github.com/Quick/Nimble) - A Matcher Framework for Swift and Objective-C :large_orange_diamond:

### A/B Testing
 * [Switchboard](https://github.com/KeepSafe/Switchboard) - Switchboard - easy and super light weight A/B testing for your mobile iPhone or android app. This mobile A/B testing framework allows you with minimal servers to run large amounts of mobile users.
 * [SkyLab](https://github.com/mattt/SkyLab) - Multivariate & A/B Testing for iOS and Mac
 * [MSActiveConfig](https://github.com/mindsnacks/MSActiveConfig) - Remote configuration and A/B Testing framework for iOS

### UI Testing
 * [CrashMonkey](https://github.com/mokemokechicken/CrashMonkey) - Monkey Test Tool For iOS.
 * [appium](http://appium.io/) - Appium is an open source test automation framework for use with native and hybrid mobile apps.
 * [robotframework-appiumlibrary](https://github.com/jollychang/robotframework-appiumlibrary) - AppiumLibrary is an appium testing library for RobotFramework.
 * [Cucumber](https://cucumber.io/) - Behavior driver development for iOS.
 * [Kif](https://github.com/kif-framework/KIF) - An iOS Functional Testing Framework.
 * [Subliminal](https://github.com/inkling/Subliminal) - An understated approach to iOS integration testing.
 * [UIAutomation](https://developer.apple.com/library/ios/documentation/DeveloperTools/Reference/UIAutomationRef/) - JavaScript library to write test scripts that exercise your app’s user interface elements while the app runs on a connected device.
 * [ios-driver](http://ios-driver.github.io/ios-driver/index.html) - Test any IOS native, hybrid, or mobile web application using Selenium / WebDriver.
 * [Zucchini](https://github.com/zucchini-src/zucchini) - A visual iOS testing framework that loves your apps.
 * [Remote](https://github.com/johnno1962/Remote) - Control your iPhone from inside Xcode for end-to-end testing.
 * [LayoutTest-iOS](https://github.com/linkedin/LayoutTest-iOS) - Write unit tests which test the layout of a view in multiple configurations :large_orange_diamond:
 * [EarlGrey](https://github.com/google/EarlGrey) - iOS UI Automation Test Framework by Google

### Other Testing
 * [NaughtyKeyboard](https://github.com/Palleas/NaughtyKeyboard) - The Big List of Naughty Strings is a list of strings which have a high probability of causing issues when used as user-input data. This is a keyboard to help you test your app from your iOS device.
 * [PonyDebugger](https://github.com/square/PonyDebugger) - Remote network and data debugging for your native iOS app using Chrome Developer Tools
 * [ios-snapshot-test-case](https://github.com/facebook/ios-snapshot-test-case) - Snapshot view unit tests for iOS.
 * [Fakery](https://github.com/vadymmarkov/Fakery) - Swift fake data generator. :large_orange_diamond:
 * [DVR](https://github.com/venmo/DVR) - Network testing for Swift :large_orange_diamond:
 * [Cuckoo](https://github.com/SwiftKit/Cuckoo) - First boilerplate-free mocking framework for Swift :large_orange_diamond:
 * [Parallel iOS Tests](https://github.com/plu/parallel_ios_tests) - Run iOS tests on multiple simulators in parallel at the same time :large_orange_diamond:
 * [Vinyl](https://github.com/Velhotes/Vinyl) - Network testing à la VCR in Swift :large_orange_diamond:

### Beta Distribution
 * [Crashlytics](https://try.crashlytics.com/) - A crash reporting and beta testing service.
 * [TestFlight Beta Testing](https://developer.apple.com/testflight/) - The beta testing service hosted on iTunes Connect (requires iOS 8 or later).
 * [HockeyApp](http://hockeyapp.net/) - With HockeyApp, you can distribute beta versions of your app, collect live crash reports, get feedback from users, and analyze test coverage.
 * [boarding](https://github.com/fastlane/boarding) - Instantly create a simple signup page for TestFlight beta testers.
 * [HockeyKit](https://github.com/bitstadium/HockeyKit) - A software update kit.

# Tools
 * [Shark](https://github.com/kaandedeoglu/Shark) - Swift Script that transforms the .xcassets folder into a type safe enum. :large_orange_diamond:
 * [R.swift](https://github.com/mac-cain13/R.swift) - Tool to get strong typed, autocompleted resources like images, cells and segues in your Swift project. :large_orange_diamond:
 * [SwiftGen](https://github.com/AliSoftware/SwiftGen) - A collection of Swift tools to generate Swift code (enums for your assets, storyboards, Localizable.strings and UIColors). :large_orange_diamond:
 * [Blade](https://github.com/jondot/blade) - Generate Xcode image catalogs for iOS / OSX app icons, universal images, and more.
 * [Retini](https://github.com/terwanerik/Retini) - A super simple retina (2x, 3x) image converter.
 * [Provisioning](https://github.com/chockenberry/Provisioning) - A Quick Look plug-in to preview .mobileprovision files.
 * [Strsync](https://github.com/metasmile/strsync) - Automatically translate and synchronize .strings files from base language.
 * [Jazzy](https://github.com/realm/jazzy) - Soulful docs for Swift & Objective-C. :large_orange_diamond:
 * [appledoc](https://github.com/tomaz/appledoc) - ObjectiveC code Apple style documentation set generator.
 * [Taylor](https://github.com/yopeso/Taylor) - Measure Swift code metrics. :large_orange_diamond:
 * [Azkaban](https://github.com/neonichu/Azkaban) - A CLI to Alcatraz, the Xcode package manager. :large_orange_diamond:
 * [Laurine](https://github.com/JiriTrecak/Laurine) - Laurine - Localization code generator written in Swift. Sweet! :large_orange_diamond:
 * [Algorithm](https://github.com/CosmicMind/Algorithm) - A toolset for writing algorithms and probability models in Swift. :large_orange_diamond:
 * [Chocolat](https://github.com/neonichu/Chocolat) - :chocolate_bar: Generate podspecs from Swift packages. :large_orange_diamond:
 * [StoryboardMerge](https://github.com/marcinolawski/StoryboardMerge) - Xcode storyboards diff and merge tool.
 * [ai2app](https://github.com/metasmile/ai2app) - Creating AppIcon sets from Adobe Illustrator (all supported formats).
 * [ViewMonitor](https://github.com/daisuke0131/ViewMonitor) - ViewMonitor can measure view positions with accuracy. :large_orange_diamond:
 * [abandoned-strings](https://github.com/ijoshsmith/abandoned-strings) - Command line program that detects unused resource strings in an iOS or OS X application. :large_orange_diamond:
 * [swiftenv](https://github.com/kylef/swiftenv) - swiftenv allows you to easily install, and switch between multiple versions of Swift. :large_orange_diamond:
 * [ThisCouldBeUsButYouPlaying](https://github.com/neonichu/ThisCouldBeUsButYouPlaying) - :black_joker: Generate Swift Playgrounds for any library. :large_orange_diamond:
 * [Misen](https://github.com/tasanobu/Misen) - Script to support easily using Xcode Asset Catalog in Swift. :large_orange_diamond:[e]
 * [git-xcp](https://github.com/metasmile/git-xcp) - A Git plugin for versioning workflow of real-world Xcode project. fastlane's best friend.
 * [WatchdogInspector](https://github.com/tapwork/WatchdogInspector) - Shows your current framerate (fps) in the status bar of your iOS app
 * [Cichlid](https://github.com/dealforest/Cichlid) - automatically delete the current project's DerivedData directories :large_orange_diamond:

# Rapid Development
 * [KZPlayground](https://github.com/krzysztofzablocki/KZPlayground) - Playgrounds for Objective-C for extremely fast prototyping / learning.
 * [MMBarricade](https://github.com/mutualmobile/MMBarricade) - Runtime configurable local server for iOS apps.
 * [NetworkObjects](https://github.com/colemancda/NetworkObjects) - Generate RESTful server from your Core Data Model.
 * [STV Framework](http://www.sensiblecocoa.com) - Native visual iOS development.

## Injection
* [dyci](https://github.com/DyCI/dyci-main) - Code injection tool.
* [injectionforxcode](https://github.com/johnno1962/injectionforxcode) - Code injection including Swift.
* [Swinject](https://github.com/Swinject/Swinject) - Dependency injection framework for Swift
* [Reliant](https://github.com/appfoundry/Reliant) - Nonintrusive Objective-C dependency injection.

# Deployment
 * [fastlane](https://github.com/fastlane/fastlane) - Connect all iOS deployment tools into one streamlined workflow.
 * [deliver](https://github.com/fastlane/fastlane/tree/master/deliver) - Upload screenshots, metadata and your app to the App Store using a single command.
 * [snapshot](https://github.com/fastlane/fastlane/tree/master/snapshot) Automate taking localized screenshots of your iOS app on every device.
 * [buddybuild](buddybuild.com) - A mobile iteration platform - build, deploy, and collaborate.
 * [Bitrise](https://www.bitrise.io) Mobile Continuous Integration & Delivery with dozens of integrations to build, test, deploy and collaborate.
 * [watchbuild](https://github.com/fastlane/fastlane/tree/master/watchbuild) - Get a notification once your iTunes Connect build is finished processing.

# App Store
 * [Average App Store Review Times](http://appreviewtimes.com) This site tracks the average App Store review times for both the iOS and the Mac App Store using data crowdsourced from iOS and Mac developers.
 * [Apple's Common App Rejections Styleguide](https://developer.apple.com/app-store/review/rejections/)  Highlighted some of the most common issues that cause apps to get rejected.
 * [Free App Store Optimization Tool](https://www.mobileaction.co) Lets you track your App Store visibility in terms of keywords and competitors.
 * [App Release Checklist](https://github.com/oisin/app-release-checklist/blob/master/checklist.md) - A checklist to pore over before you ship that amazing app that has taken ages to complete, but you don't want to rush out in case you commit a schoolboy error that will end up making you look dumber than you are.
 * [Harpy](https://github.com/ArtSabintsev/Harpy) - Notify users when a new version of your iOS app is available, and prompt them with the App Store link.
 * [iRate](https://github.com/nicklockwood/iRate) - A handy class that prompts users of your iPhone or Mac App Store app to rate your application after using it for a while. Similar to Appirater, but with a simpler, cleaner interface and automatic support for iOS fast application switching.

# SDK

## Official

 * [Spotify](https://github.com/spotify/ios-sdk) Spotify iOS SDK.
 * [Facebook](https://github.com/facebook/facebook-ios-sdk) Facebook iOS SDK.
 * [Google Analytics](https://developers.google.com/analytics/devguides/collection/ios/v3/) Google Analytics SDK for iOS
 * [Paypal iOS SDK](https://github.com/paypal/PayPal-iOS-SDK) The PayPal Mobile SDKs enable native apps to easily accept PayPal and credit card payments.
 * [Pocket](https://github.com/Pocket/Pocket-ObjC-SDK) SDK for saving stuff to Pocket.
 * [Tumblr](https://github.com/tumblr/TMTumblrSDK) Library for easily integrating Tumblr data into your iOS or OS X application.
 * [Evernote](https://github.com/evernote/evernote-cloud-sdk-ios) Evernote SDK for iOS.
 * [Box](https://github.com/box/box-ios-sdk) iOS + OS X SDK for the Box API.
 * [OneDrive](https://github.com/OneDrive/onedrive-sdk-ios) Live SDK for iOS.
 * [Stripe](https://github.com/stripe/stripe-ios) Stripe bindings for iOS and OS X.
 * [Venmo](#payments)
 * [AWS](https://github.com/aws/aws-sdk-ios) Amazon Web Services Mobile SDK for iOS.
 * [Zendesk](https://github.com/zendesk/zendesk_sdk_ios) Zendesk Mobile SDK for iOS.
 * [Adobe Creative SDK](https://creativesdk.adobe.com/) Adobe creative tools and Creative Cloud SDK.
 * [Dropbox](https://www.dropbox.com/developers) SDKs for Drop-ins and Dropbox Core API.
 * [Fabric by Twitter](https://docs.fabric.io/ios/index.html) Fabric Twitter Kit for iOS.
 * [Liquid Analytics](https://github.com/lqd-io/liquid-sdk-ios) Identify behaviours through Analytics and react with real-time Personalization.
 * [ResearchKit](https://github.com/ResearchKit/ResearchKit) ResearchKit is an open source software framework that makes it easy to create apps for medical research or for other research projects.
 * [PacketZoom](https://packetzoom.com) PacketZoom SDK for iOS.
 * [Primer](https://www.goprimer.com) - Easy SDK for creating personalized landing screens, signup, and login flows on a visual editor with built in a/b/n testing and analytics.
 * [Azure](https://github.com/Azure/azure-storage-ios) - Client library for accessing Azure Storage on an iOS device
 * [1Password](https://github.com/AgileBits/onepassword-app-extension) - 1Password Extension for iOS Apps

## Unofficial

 * [STTwitter](https://github.com/nst/STTwitter) A stable, mature and comprehensive Objective-C library for Twitter REST API 1.1
 * [FHSTwitterEngine](https://github.com/fhsjaagshs/FHSTwitterEngine) Twitter API for Cocoa developers.
 * [Giphy](https://github.com/heyalexchoi/Giphy-iOS) Giphy API client for iOS in Objective-C.
 * [UberKit](https://github.com/sachinkesiraju/UberKit) - A simple, easy-to-use Objective-C wrapper for the Uber API.
 * [InstagramKit](https://github.com/shyambhat/InstagramKit) - Instagram iOS SDK.
 * [DribbbleSDK](https://github.com/agilie/dribbble-ios-sdk) - Dribbble iOS SDK.
 * [objectiveflickr](https://github.com/lukhnos/objectiveflickr) - ObjectiveFlickr, a Flickr API framework for Objective-C.
 * [Easy Social](https://github.com/pjebs/EasySocial) - Twitter & Facebook Integration.
 * [das-quadrat](https://github.com/Constantine-Fry/das-quadrat) - A Swift wrapper for Foursquare API. iOS and OSX. :large_orange_diamond:
 * [SocialLib](https://github.com/darkcl/SocialLib) - SocialLib handles sharing message to multiple social media.
 * [PokemonKit](https://github.com/ContinuousLearning/PokemonKit) - Pokeapi wrapper, written in Swift :large_orange_diamond:
 
# Xcode

### Plugins
 * [FuzzyAutocompletePlugin](https://github.com/FuzzyAutocomplete/FuzzyAutocompletePlugin) - A Xcode 5+ plugin that adds more flexible autocompletion rather than just prefix-matching.
 * [SCXcodeMiniMap](https://github.com/stefanceriu/SCXcodeMiniMap) - SCXcodeMiniMap is a plugin that adds a source editor MiniMap to Xcode.
 * [Show in Github](https://github.com/larsxschneider/ShowInGitHub) - Xcode plugin to open the GitHub page of the commit of the currently selected line in the editor window.
 * [BBUFullIssueNavigator](https://github.com/neonichu/BBUFullIssueNavigator) - Xcode plugin for showing all issue content in the issue navigator.
 * [BBUDebuggerTuckAway](https://github.com/neonichu/BBUDebuggerTuckAway) - Xcode plugin for auto-hiding the debugger once you start typing in the source code editor.
 * [SCXcodeSwitchExpander](https://github.com/stefanceriu/SCXcodeSwitchExpander) - SCXcodeSwitchExpander is a small Xcode plugin that expands switch statements by inserting missing cases.
 * [VVDocumenter-Xcode](https://github.com/onevcat/VVDocumenter-Xcode) - Xcode plug-in which helps you write Javadoc style documents easier.
 * [XAlign](https://github.com/qfish/XAlign) - An amazing Xcode plugin to align regular code. It can align anything by using custom alignment patterns.
 * [CocoaPods Xcode Plugin](https://github.com/kattrali/cocoapods-xcode-plugin) - Dependency management helper for your CocoaPods, right in Xcode.
 * [KSImageNamed-Xcode](https://github.com/ksuther/KSImageNamed-Xcode) - Xcode plug-in that provides autocomplete for imageNamed: calls.
 * [ColorSense-for-Xcode](https://github.com/omz/ColorSense-for-Xcode) - Plugin for Xcode to make working with colors more visual.
 * [Backlight-for-XCode](https://github.com/limejelly/Backlight-for-XCode) - Highlights the current editing line in Xcode
 * [KPRunEverywhereXcodePlugin](https://github.com/kitschpatrol/KPRunEverywhereXcodePlugin) - An Xcode plugin to build and run an app across multiple iOS devices with one click.
 * [RevealPlugin](https://github.com/shjborage/Reveal-Plugin-for-Xcode) - Plugin for Xcode to integrate the Reveal App to your project automatic.
 * [RealmPlugin](https://realm.io/docs/objc/0.81.0/#xcode-plugin)- Xcode plugin to generate new Realm models.
 * [AdjustFontSize](https://github.com/zats/AdjustFontSize-Xcode-Plugin) - Instant font size adjustment with `⌘ +` / `⌘ -`.
 * [Rephrase](https://www.rephrase.io) - Localise from Xcode.
 * [XCActionBar](https://github.com/pdcgomes/XCActionBar) - "Alfred for Xcode" plugin.
 * [QuickJump](https://github.com/wiruzx/QuickJump) - Quick code navigation for Xcode.
 * [CATweaker](https://github.com/keefo/CATweaker) - Plugin for creating beautiful CAMediaTimingFunction curve.
 * [XcodeWay](https://github.com/onmyway133/XcodeWay) - An Xcode plugin that makes navigating to many places easier (available via Alcatraz).
 * [GitDiff](https://github.com/johnno1962/GitDiff) - Highlights deltas against git repo in Xcode.
 * [MCLog](https://github.com/yuhua-chen/MCLog) - Xcode plugin for filtering the console area.
 * [XToDo](https://github.com/trawor/XToDo) - Dialog with list of all TODO, FIXME, ??? and !!! in the project.
 * [CopyIssue](https://github.com/hanton/CopyIssue-Xcode-Plugin) - Makes Copy Xcode Issue Description Easy.
 * [RTImageAssets](https://github.com/rickytan/RTImageAssets) - A Xcode plugin to automatically generate all the App icons needed.
 * [BBUncrustifyPlugin-Xcode](https://github.com/benoitsan/BBUncrustifyPlugin-Xcode) - Xcode plugin to format source code using ClangFormat or Uncrustify.
 * [Aviator](https://github.com/marksands/Aviator) - Xcode plugin that brings ⇧⌘T (source/test toggle) from AppCode over to Xcode.
 * [JumpMarks](https://github.com/merrickp/JumpMarks) - Navigate your code files with numbered bookmarks.
 * [XCSnippetr](https://github.com/dzenbot/XCSnippetr) - An Xcode Plugin to upload code snippets directly into Slack and Gist.
 * [Peckham](https://github.com/markohlebar/Peckham) - Add #import-s from anywhere in the code.
 * [MLAutoReplace](https://github.com/molon/MLAutoReplace) - Xcode plugin, Re-Intent, make you write code more quickly.
 * [AutoHighlightSymbol](https://github.com/chiahsien/AutoHighlightSymbol) - A Xcode plugin to add highlight to the instances of selected symbol.
 * [Reveal-In-GitHub](https://github.com/lzwjava/Reveal-In-Github) - Xcode plugin to let you jump to GitHub History, Blame, PRs, Issues, Notifications of any GitHub repo with one shortcut.
 * [CleanHeaders-Xcode](https://github.com/insanoid/CleanHeaders-Xcode) - A simple iSort like header sorting and duplicate removal plugin for Xcode, makes your headers look more organized.
 * [Luft](https://github.com/k0nserv/luft) - The Xcode Plugin that helps you write lighter view controllers
 * [You-Can-Do-It](https://github.com/orta/You-Can-Do-It) - Is learning a new language getting you down? Worry not, this Xcode plugin will keep you motivated.
 * [PreciseCoverage](https://github.com/zats/PreciseCoverage) - Make Xcode code coverage more informative
 * [AutoIndentWithSave](https://github.com/ThilinaHewagama/AutoIndentWithSave) Xcode plugin which indent the source code when save
 * [Refactorator](https://github.com/johnno1962/Refactorator) - SourceKit Xcode Plugin that Refactors Swift :large_orange_diamond:
 * [VWInstantRun](https://github.com/wangshengjia/VWInstantRun) - An Xcode plugin let you build & run your selected lines of code in Xcode without running the whole project, you'll have the output instantly in your Xcode console. :large_orange_diamond:
 * [TTPasteHistory](https://github.com/tutumagi/TTPasteHistory) - A Xcode plugin. Recording you copy-and-paste history easily to write the code
 * [xSendIssue](https://github.com/hungri-yeti/xSendIssue) - Plugin for Xcode to submit github issues directly from within Xcode.
 * [Swimat](https://github.com/Jintin/Swimat) - An Xcode formatter plug-in to format your swift code.
 * [Fastlane-Plugin](https://github.com/RishabhTayal/Fastlane-Plugin) - The awesome Fastlane tools brought into your Xcode.

### Themes
 * [Dracula Theme](https://github.com/zenorocha/dracula-theme) - A dark theme for Xcode.
 * [Xcode themes list](https://github.com/hdoria/xcode-themes) - Color themes for Xcode.
 * [Solarized-Dark-for-Xcode](https://github.com/ArtSabintsev/Solarized-Dark-for-Xcode/) - Solarized Dark Theme for Xcode 5.

### Other Xcode
 * [Synx](https://github.com/venmo/synx) - A command-line tool that reorganizes your Xcode project folder to match your Xcode groups.
 * [dsnip](https://github.com/Tintenklecks/IBDelegateCodesippets) - Tool to generate (native) Xcode code snippets from all protocols/delegate methods of UIKit (UITableView, ...)
 * [SBShortcutMenuSimulator](https://github.com/DeskConnect/SBShortcutMenuSimulator) - 3D Touch shortcuts in the Simulator


# Style Guides
* [NY Times - Objective C Style Guide](https://github.com/NYTimes/objective-c-style-guide) - The Objective-C Style Guide used by The New York Times.
* [raywenderlich Style Guide](https://github.com/raywenderlich/objective-c-style-guide) - A style guide that outlines the coding conventions for raywenderlich.com.
* [Github Objective-C Style Guide](https://github.com/github/objective-c-style-guide) - Style guide & coding conventions for Objective-C projects.
* [Objective-C Coding Convention and Best Practices](https://gist.github.com/soffes/812796) - Gist with coding conventions.
* [Swift Style Guide by @raywenderlich](https://github.com/raywenderlich/swift-style-guide) - The official Swift style guide for raywenderlich.com. :large_orange_diamond:
* [Spotify Objective-C Coding Style](https://github.com/spotify/ios-style) - Guidelines for iOS development in use at Spotify.
* [Dropbox Objective-C Style Guide](https://dl.dropboxusercontent.com/s/5utnlwhr18ax05c/style-guide.html?dl=0) -
* [Github - Style guide & coding conventions for Swift projects](https://github.com/github/swift-style-guide) - A guide to our Swift style and conventions by @github. :large_orange_diamond:
* [Futurice iOS Good Practices](https://github.com/futurice/ios-good-practices) - iOS starting guide and good practices suggestions by [@futurice](https://github.com/futurice).
* [Swift-Community-Best-Practices](https://github.com/schwa/Swift-Community-Best-Practices/) - Best practices for software development with Swift :large_orange_diamond:
* [SlideShare Swift Style Guide](https://github.com/SlideShareInc/swift-style-guide/blob/master/swift_style_guide.md) - SlideShare Swift Style Guide we are using for our upcoming iOS 8 only app written in Swift :large_orange_diamond:
* [Prolific Interactive Style Guide](https://github.com/prolificinteractive/swift-style-guide) - A style guide for Swift made by Prolific Interactive :large_orange_diamond:

# Good Websites

### News, Blogs and more
 * [BGR](http://bgr.com/ios-7/)
 * [iMore](http://www.imore.com/)
 * [Lifehacker](http://lifehacker.com/tag/ios)
 * [NSHipster](http://nshipster.com)
 * [Objc.io](https://www.objc.io/)
 * [ASCIIwwdc](http://asciiwwdc.com)
 * [Natasha The Robot](https://www.natashatherobot.com/)
 * [Apple's Swift Blog](https://developer.apple.com/swift/blog/) :large_orange_diamond:
 * [iOS Programming Subreddit](https://www.reddit.com/r/iosprogramming)
 * [iOS Dev Weekly](https://iosdevweekly.com/)
 * [iOS8-day-by-day](https://github.com/shinobicontrols/iOS8-day-by-day) :large_orange_diamond:
 * [iOScreator](http://www.ioscreator.com/) :large_orange_diamond:
 * [Mathew Sanders](http://mathewsanders.com/) :large_orange_diamond:
 * [Little Bites of Cocoa](https://littlebitesofcocoa.com/) :large_orange_diamond:
 * [iOS Dev Nuggets](http://hboon.com/iosdevnuggets/) :large_orange_diamond:
 * [This Week in Swift](http://swiftnews.curated.co) :large_orange_diamond:
 * [iOS Developer and Designer interview](https://github.com/CameronBanga/iOS-Developer-and-Designer-Interview-Questions) - A small guide to help those looking to hire a developer or designer for iOS work.
 * [iOS9-day-by-day](https://github.com/shinobicontrols/iOS9-day-by-day) :large_orange_diamond:

### UIKit references
 * [iOS Fonts](http://iosfonts.com/)
 * [UIAppearance list](https://gist.github.com/mattt/5135521)

### Forums and discuss lists
 * [iPhone Dev SDK Forum](http://iphonedevsdk.com/)
 * ["iOS" on Stackoverflow](http://stackoverflow.com/questions/tagged/ios)

### Tutorials and Keynotes
 * [AppCoda](http://www.appcoda.com)
 * [Tutorials Point](http://www.tutorialspoint.com/ios/)
 * [Code with Cris](http://codewithchris.com/)
 * [Cocoa with Love](http://www.cocoawithlove.com/)
 * [Cocoa is my Girlfriend](http://www.cimgf.com/)
 * [Code School - Try Objective-C](http://tryobjectivec.codeschool.com/)
 * [Brian Advent youtube channel](https://www.youtube.com/channel/UCysEngjfeIYapEER9K8aikw/videos) - Swift tutorials Youtube Channel. :large_orange_diamond:
 * [RAYWENDERLICH](https://www.raywenderlich.com/tutorials) - Tutorials for developers and gamers
 * [Ry’s Objective-C Tutorial](http://rypress.com/tutorials/objective-c/index)
 * [Mike Ash](https://www.mikeash.com/pyblog/)
 * [Big Nerd Ranch](https://www.bignerdranch.com/blog/categories/ios/) :large_orange_diamond:
 * [Tuts+](http://code.tutsplus.com/categories/ios-sdk) :large_orange_diamond:
 * [iOS-Blog](http://www.ios-blog.co.uk/) :large_orange_diamond:
 * [Thinkster](https://thinkster.io/a-better-way-to-learn-swift) :large_orange_diamond:
 * [Swift Education](https://github.com/swifteducation) - A community of educators sharing materials for teaching Swift and app development. :large_orange_diamond:
 * [Cocoa Dev Central](http://cocoadevcentral.com)
 * [Use Your Loaf](http://useyourloaf.com)
 * [Swift Tutorials by Jameson Quave](http://jamesonquave.com/blog/tutorials/) :large_orange_diamond:
 * [Awesome-Swift-Education](https://github.com/hsavit1/Awesome-Swift-Education) - :fire: All of the resources for Learning About Swift :large_orange_diamond:
 * [Awesome-Swift-Playgrounds](https://github.com/uraimo/Awesome-Swift-Playgrounds) - A List of Awesome Swift Playgrounds! :large_orange_diamond:
 * [learn-swift](https://github.com/nettlep/learn-swift) - Learn Apple's Swift programming language interactively through these playgrounds. :large_orange_diamond:

### iOS UI Template
 * [App Icon Template](http://appicontemplate.com/ios8/)
 * [iOS 8 GUI PSD Template](http://www.teehanlax.com/tools/iphone/)
 * [iOS UI Design Kit](https://www.invisionapp.com/tethr)
 * [iOS Design Guidelines](http://iosdesign.ivomynttinen.com/)

### Prototyping
 * [FluidUI](https://www.fluidui.com)
 * [Proto.io](https://proto.io/)
 * [Framer](http://framerjs.com/)
 * [Pixate](http://www.pixate.com/)
 * [Principle](http://principleformac.com)

### Newsletters
 * [iOS Goodies](http://ios-goodies.com) - Weekly iOS newsletter
 * [This Week in Swift](https://swiftnews.curated.co) - I'm @NatashaTheRobot and I'm programmed to love #Swift! Every week, I put together a list of the best Swift resources for you. Happy Learning!
 * [The iOS Times](http://theiostimes.com) - A weekly publication with news and trending projects in the open source iOS ecosystem.
 * [Swift Sandbox](http://swiftsandbox.io) - Swift developer newsletter, curated collection of Swift open source news, projects & resources. :large_orange_diamond:
 * [raywenderlich.com Weekly](https://www.raywenderlich.com/newsletter) - sign up to receive the latest tutorials from raywenderlich.com each week
 * [iOS Dev Tools Weekly](https://iosdev.tools) - The greatest iOS development tools, including websites, desktop and mobile apps, and back-end services.
 * [iOS Trivia Weekly](http://wanderbit.us4.list-manage.com/subscribe?u=4e20cd8ea3a0ce09ff4619a52&id=5898a5992b) - Three challenging questions about iOS development every Wednesday
 * [Indie iOS Focus Weekly](https://indieiosfocus.curated.co) - Looking for the best iOS dev links, tutorials, & tips beyond the usual news? Curated by Chris Beshore. Published every Thursday.

### Medium
 * [iOS App Development](https://medium.com/ios-os-x-development) - Stories and technical tips about building apps for iOS, Apple Watch, and iPad/iPhone
 * [Swift Programming](https://medium.com/swift-programming) - The Swift Programming Language

# Twitter
 * [@objcio](https://twitter.com/objcio)
 * [@nshipster](https://twitter.com/NSHipster)
 * [@CocoaPods](https://twitter.com/CocoaPods)
 * [@CocoaPodsFeed](https://twitter.com/CocoaPodsFeed)
 * [@RubyMotion](https://twitter.com/RubyMotion)
 * [@SwiftSandbox](https://twitter.com/SwiftSandbox) - Swift open source news, projects and resources.


# Facebook Groups
 * [HH iOS](https://www.facebook.com/groups/hhios/)
 * [Sketch - Official group](https://www.facebook.com/groups/sketchformac/)
 * [Design-Code](https://www.facebook.com/groups/designcode/)
 * [Sketch-Design.io](https://www.facebook.com/groups/sketchdesignio)
 * [Origami Community](https://www.facebook.com/groups/origami.community/)
 * [Framer JS](https://www.facebook.com/groups/framerjs/)

# Podcasts
 * [The Ray Wenderlich Podcast](https://www.raywenderlich.com/rwpodcast)
 * [Debug](http://www.imore.com/debug)
 * [iDeveloper](http://ideveloper.co/)
 * [App Story](http://www.appstorypodcast.com)
 * [Mobile Couch](http://mobilecouch.co/)
 * [iOS Bytes](https://iosbytes.codeschool.com/)
 * [iPhreaks](https://devchat.tv/iphreaks)

# Books
 * [The Swift Programming Language by Apple](https://itunes.apple.com/us/book/swift-programming-language/id881256329?mt=11) :large_orange_diamond:
 * [Using Swift with Cocoa and Objective C by Apple](https://itunes.apple.com/us/book/using-swift-cocoa-objective/id888894773?mt=11) :large_orange_diamond:
 * [iOS Programming: The Big Nerd Ranch Guide by Christian Keur, Aaron Hillegass, Joe Conway](https://www.bignerdranch.com/we-write/ios-programming/)
 * [Programming in Objective-C by Stephen G. Kochan](http://www.amazon.com/Programming-Objective-C-6th-Developers-Library/dp/0321967607)
 * [Your First iOS App by Ash Furrow](https://leanpub.com/your-first-ios-app)
 * [The Complete Friday Q & A: Volume 1](https://www.mikeash.com/book.html)
 * [Core Data for iOS: Developing Data-Driven Applications for the iPad, iPhone, and iPod touch](http://www.amazon.com/Core-Data-iOS-Data-Driven-Applications/dp/0321670426/)
 * [Cocoa Design Patterns](http://www.amazon.com/Cocoa-Design-Patterns-Erik-Buck/dp/0321535022)

# Other Awesome Lists
Other amazingly awesome lists can be found in the
 * [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) list.
 * [Open Source apps](https://github.com/dkhamsing/open-source-ios-apps) list of open source ios apps
 * Awesome-swift
   * [@matteocrippa](https://github.com/matteocrippa/awesome-swift) - A collaborative list of awesome swift resources.
   * [@Wolg](https://github.com/Wolg/awesome-swift) - A curated list of awesome Swift frameworks, libraries and software.
   * [Education](https://github.com/hsavit1/Awesome-Swift-Education) - All the resources you need to learn Swift
 * [awesome watchkit apps](https://github.com/sanketfirodiya/sample-watchkit-apps) curated list of sample watchkit apps and tutorials. :watch:
 * [iOS Learning Resources](https://github.com/sanketfirodiya/iOS-learning-resources) Comprenehensive collection of high quality, frequently updated and well maintained iOS tutorial sites.
 * [awesome-ios-animation](https://github.com/sxyx2008/awesome-ios-animation) - A curated list of awesome iOS animation, including Objective-C and Swift libraries.
 * [awesome-ios-chart](https://github.com/sxyx2008/awesome-ios-chart) - A curated list of awesome iOS chart libraries, including Objective-C and Swift.
 * [awesome-gists](https://github.com/vsouza/awesome-gists#ios) - A list of amazing gists (iOS section).
 * [awesome-ios-ui](https://github.com/cjwirth/awesome-ios-ui) - A curated list of awesome iOS UI/UX libraries.
 * [Awesome Reactive Programming in Swift](https://github.com/SideEffects-xyz/Awesome-Reactive-Programming-Swift) - A collection of frameworks, talks and resources about reactive programming in Swift.

# Contributing
[See the guide](https://github.com/vsouza/awesome-ios/blob/master/CONTRIBUTING.md)

# License
<a rel="license" href="http://creativecommons.org/publicdomain/mark/1.0/">
<img src="https://licensebuttons.net/p/mark/1.0/88x31.png"
     style="border-style: none;" alt="Public Domain Mark" />
</a>

To the extent possible under law, [Vinicius Souza](https://github.com/vsouza) has waived all copyright and related or neighboring rights to this work.
