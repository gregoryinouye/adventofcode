#!/usr/bin/env kotlin

/**
 * https://adventofcode.com/2020/day/3
 */

import java.io.FileReader
import java.io.FileNotFoundException
import java.lang.RuntimeException

fun readData(): List<String> {
    return FileReader("./2020-04.txt").readLines()
}

val input = readData()

val passports = mutableMapOf<Int, String>()
var count = 0
for (line in input) {
    count
    if (line == "") {
        count++
        continue
    }

    val existing = passports.get(count)
    existing?.let {
        passports.put(count, "$existing $line")
    } ?: passports.put(count, line)
}

var validCount = 0

for (passport in passports.values) {
    val categories = mutableSetOf("cid")
    passport.split(":", " ").forEachIndexed {
        i, value -> if (i % 2 == 0) categories.add(value)
    }
    if (categories.size == 8) validCount++
}

println(validCount)

/**
 * Part 2
 */

validCount = 0

for (passport in passports.values) {
    val categories = mutableSetOf("cid")

    val data = passport.split(":", " ")
    for (i in 0..data.size-1) {
        val value = data[i]
        if (i % 2 == 0) {
            when (value) {
                "byr" -> {
                    println("byr")
                    val year = data[i + 1].toInt()
                    println(year)
                    if (year >= 1920 && year <= 2002) {
                        categories.add(value)
                        println(true)
                    }
                }
                "iyr" -> {
                    val year = data[i + 1].toInt()
                    if (year >= 2010 && year <= 2020) categories.add(value)
                }
                "eyr" -> {
                    val year = data[i + 1].toInt()
                    if (year >= 2020 && year <= 2030) categories.add(value)
                }
                "hgt" -> {
                    val height = data[i + 1]
                    when (height.substring(height.count() - 2, height.count())) {
                        "cm" -> {
                            val ht = height.substring(0, height.count() - 2).toInt()
                            if (ht >= 150 && ht <= 193) categories.add(value)
                        }
                        "in" -> {
                            val ht = height.substring(0, height.count() - 2).toInt()
                            if (ht >= 59 && ht <= 76) categories.add(value)
                        }
                    }
                }
                "hcl" -> {
                    val hair = data[i + 1]
                    val chars = setOf('a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

                    if (hair[0] == '#' && hair.substring(1, hair.count()).all { it in chars }) categories.add(value)
                }
                "ecl" -> {
                    val eye = data[i + 1]
                    if (eye in setOf("amb", "blu", "brn", "gry", "grn", "hzl", "oth")) categories.add(value)
                }
                "pid" -> {
                    val pass = data[i + 1]
                    if (pass.count() == 9 && pass.all { it in setOf('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') }) categories.add(value)
                }
            }
        }
    }
    if (categories.size == 8) validCount++
}

println(validCount)
