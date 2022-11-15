<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" 
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:wikidata="https://www.wikidata.org/wiki/"
    xmlns:geonames="https://www.geonames.org/"
    xmlns:viaf="http://viaf.org/viaf/"
    xmlns:foaf="http://xmlns.com/foaf/0.1/" exclude-result-prefixes="xs" version="1.0">
    <xsl:output method="html"/>
    <xsl:strip-space elements="app-realia-list"/>
    
    <!-- teiHeader -->
    <xsl:template match="tei:teiHeader"> </xsl:template>
   
 
    
    <!-- persons list -->
    <xsl:template name="person-list">
        <ul>
            <xsl:for-each
                select="/tei:TEI/tei:teiHeader/tei:profileDesc/tei:particDesc/tei:listPerson/tei:person/tei:persName">
                <xsl:sort order="ascending"/>
                <li>
                    <xsl:value-of select="."/>
                </li>
            </xsl:for-each>
        </ul>
    </xsl:template>
   
    
    <!-- persName -->
    <xsl:template match="tei:persName">
        <span class="pers-name">
            <xsl:apply-templates/>
        </span>
    </xsl:template>
    
    
    <xsl:template match="tei:date">
        <span class="date">
            <xsl:apply-templates/>
        </span>
    </xsl:template>

    
    <!-- head -->
    <xsl:template match="tei:head">
        <h5>
            <xsl:apply-templates/>
        </h5>
    </xsl:template>
    
    <!-- p -->
    <xsl:template match="tei:p">
        <p>
            <xsl:apply-templates/>
        </p>
    </xsl:template>
    
    <!-- div -->
    <xsl:template match="tei:div">
        <div>
            <xsl:attribute name="id">
                <xsl:value-of select="@xml:id"/>
            </xsl:attribute>
            <xsl:attribute name="class">chap</xsl:attribute>
            <xsl:apply-templates/>
        </div>
    </xsl:template>
    
    <!-- body -->
    <xsl:template match="tei:body">
        <article>
            <xsl:apply-templates/>
        </article>
    </xsl:template>
    
    <!-- catch-all -->
    <xsl:template match="*">
        <xsl:message terminate="no">WARNING: Unmatched element: <xsl:value-of select="name()"/>
        </xsl:message>
        <xsl:apply-templates/>
    </xsl:template>
    
    <!-- root template -->
    <xsl:template match="/tei:TEI">
        <xsl:text disable-output-escaping="yes">&lt;!DOCTYPE html&gt;</xsl:text>
        <xsl:variable name="title"
            select="/tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title"/>
        <html>
            <head>
                <meta charset="utf-8"/>
                <meta name="description" content="TEI Sample"/>
                <meta name="viewport" content="width=device-width, initial-scale=1"/>
                <title>
                    <xsl:value-of select="$title"/>
                </title>
            </head>
            <body>
                <h1>
                    <xsl:value-of select="$title"/>
                </h1>
                <xsl:apply-templates/>
                <hr/>
                <h2>Persons Index</h2>
                <xsl:call-template name="person-list"></xsl:call-template>               
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
