<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="xml" indent="yes"/>
<xsl:param name="derailers-per-page" select="5"/>

<!-- document --> 
<xsl:template match="/">
 <xsl:element name="document">
   <xsl:call-template name="Pager"/>
 </xsl:element>
</xsl:template>


<!-- *****************************************************
       pager test
     *****************************************************  -->
<xsl:template name="Pager" >
<xsl:variable name="drcount" select="count(raw_scores/scores/*)"/>
<xsl:choose>
    <xsl:when test="$drcount > 5">
        <xsl:call-template name="FirstPage"/>
        <xsl:call-template name="SecondPage"/>
    </xsl:when>
    <xsl:otherwise>
        <xsl:call-template name="FirstPage"/>
    </xsl:otherwise>
</xsl:choose>
</xsl:template>

<xsl:template name="FirstPage" >
    <blockTable style="SimpleTable">
    <xsl:for-each select="raw_scores/scores/*">
        <xsl:choose>
            <xsl:when test="position() &lt; 6">
                <xsl:call-template name="DerailerRow"/>
            </xsl:when>
            <xsl:otherwise>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:for-each>
    </blockTable>
</xsl:template>

<xsl:template name="SecondPage" >
    <blockTable style="ComplexTable">
    <xsl:for-each select="raw_scores/scores/*">
        <xsl:choose>
            <xsl:when test="position() &gt; 5">
                <xsl:call-template name="DerailerRow"/>
            </xsl:when>
            <xsl:otherwise>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:for-each>
    </blockTable>
</xsl:template>

<xsl:template name="DerailerRow" >
    <tr>
        <td align="left" fontSize="7">
            <xsl:value-of select="current()/attr_name"/>
        </td>
        <td align="left" fontSize="7">
            <para style="byeline"><xsl:value-of select="current()/definition_stmt"/></para>
        </td>
        <td align="left" fontSize="7">
            <para style="byeline"><xsl:value-of select="current()/derailer_stmt"/></para>
        </td>
    </tr>
</xsl:template>


<!-- *****************************************************
                        THE END 
     *****************************************************  -->
</xsl:stylesheet>
