#!/usr/bin/env kotlin

import java.io.FileReader

fun readData(): List<String> {
    return FileReader("./2015-02.txt").readLines()
}

val input = readData().map { present -> present.split("x").map { it.toInt() } }

fun calculateWrappingPaper(length: Int, height: Int, width: Int): Int {
    val sideOne = 2 * height * length
    val sideTwo = 2 * height * width
    val sideThree = 2 * length * width
    val minimum: Int = minOf(sideOne, sideTwo, sideThree) / 2

    return sideOne + sideTwo + sideThree + minimum
}

var paper: Int = 0
var ribbon: Int = 0

for ((l, h, w) in input) {
    paper += calculateWrappingPaper(l, h, w)
    ribbon += calculateRibbon(l, h, w)
}

println("Part One: $paper")
// 1588178

fun calculateRibbon(length: Int, height: Int, width: Int): Int {
    val lengths = listOf(length, height, width).sorted()
    return 2 * (lengths[0] + lengths[1]) + length * height * width
}

println("Part Two: $ribbon")
// 3783758
