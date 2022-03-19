#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2021/day/3
 */

import java.io.FileReader
import java.io.FileNotFoundException

fun readInput(): List<String> {
    return FileReader("./2021-03.txt").readLines()
}

val input = readInput()

val binaryLength = input.first().length

val oneCount = MutableList(binaryLength) { 0 }

input.forEach { binary ->
    binary.forEachIndexed { index, value -> oneCount[index] += Character.getNumericValue(value) }
    }

val invertCount = MutableList(binaryLength) { index -> binaryLength - oneCount[index] }

println(oneCount)
print(invertCount)


//var zero = mutableListOf(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
//var one =  mutableListOf(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
//
//input.forEach { word ->
//    word.forEachIndexed { index, letter -> if (letter == '1') one[index]++ else zero[index]++ }
//}
//
//println(zero)
//println(one)
//
//val gamma = zero.mapIndexed { index, letter -> if (zero[index] > one[index]) '0' else '1' }.joinToString("")
//val epsilon = zero.mapIndexed { index, letter -> if (zero[index] < one[index]) '0' else '1' }.joinToString("")
//
//println(gamma.toInt(2))
//println(epsilon.toInt(2))


//println(gamma.toInt(2) * epsilon.toInt(2))

/**
 * Part 2
 */

//var zero = mutableListOf(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
//var one = mutableListOf(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
//
//var filtered = input
//var index = 0
//
//while (filtered.size > 1) {
//    filtered.forEach { word -> if (word[index] == '1') one[index]++ else zero[index]++ }
//    filtered = filtered.filter { if (zero[index] <= one[index]) it[index] == '0' else it[index] == '1' }
//    index++
//}
//
//println(filtered.first().toInt(2))

// 000011011011 -> 219
// 1459
// 3178