<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml"/>

    <xsl:template match="/">
    <temp_rawscores>
      <xsl:apply-templates select="raw_scores"/>
    </temp_rawscores>
    </xsl:template>

    <xsl:template match="raw_scores">
    <scores>
      <xsl:apply-templates select="scores/QuestandResp"/>
    </scores>
    </xsl:template>

    <xsl:template match="QuestandResp">
    <!-- 
        <rs><xsl:value-of select="question_id"/> resp="<xsl:value-of select="response"/>"</rs>'   -->
        <xsl:element name=<xsl:value-of select="question_id"/> ></xsl:element>
    </xsl:template>

</xsl:stylesheet>
