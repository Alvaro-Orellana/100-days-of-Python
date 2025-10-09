fun itDoesSomethingAlso(elements: List<String>): List<Pair<String, Int>> {
    return elements.groupBy {
        it
    }.map {
        Pair(it.key, it.value.count())
    }
}

func itDoesSomethingAlso(elements: [String]) -> [(String, Int)] {
    elements.map { element in (element, element.count) }
}