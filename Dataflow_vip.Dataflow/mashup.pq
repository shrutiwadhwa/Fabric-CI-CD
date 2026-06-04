[DefaultOutputDestinationSettings = [DestinationDefinition = [Kind = "Reference", QueryName = "DefaultDestination", IsNewTarget = true], UpdateMethod = [Kind = "Replace"], DestinationTypeSettings = [Kind = "File", TransformationQueryName = "DefaultDestination_DataDestinationTransform"]], StagingDefinition = [Kind = "FastCopy"]]
section Section1;
shared DefaultDestination = let
  Source = AzureStorage.DataLake("https://shruadls.dfs.core.windows.net/", [HierarchicalNavigation = true]),
  #"Navigation 1" = Source{[Name = "input"]}[Content]
in
  #"Navigation 1";
shared DefaultDestination_DataDestinationTransform = Csv.OutputConfiguration([Encoding = 65001, Delimiter = ","]);
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "Query_DataDestination", IsNewTarget = true], Settings = [Kind = "Manual", AllowCreation = true, ColumnSettings = [Mappings = {[SourceColumnName = "customer_id", DestinationColumnName = "customer_id"], [SourceColumnName = "firstName", DestinationColumnName = "firstName"], [SourceColumnName = "lastName", DestinationColumnName = "lastName"], [SourceColumnName = "gender", DestinationColumnName = "gender"], [SourceColumnName = "age", DestinationColumnName = "age"], [SourceColumnName = "city", DestinationColumnName = "city"], [SourceColumnName = "state", DestinationColumnName = "state"], [SourceColumnName = "customer_segment", DestinationColumnName = "customer_segment"], [SourceColumnName = "onboarding_date", DestinationColumnName = "onboarding_date"], [SourceColumnName = "kyc_status", DestinationColumnName = "kyc_status"]}], DynamicSchema = false, UpdateMethod = [Kind = "Replace"], TypeSettings = [Kind = "Table"]]]}]
shared Query = let
  Source = AzureStorage.DataLake("https://shruadls.dfs.core.windows.net/"),
  Navigation = Source{[#"Folder Path" = "https://shruadls.dfs.core.windows.net/input/", Name = "customers.csv"]}[Content],
  #"Imported CSV" = Csv.Document(Navigation, [Delimiter = ",", Columns = 9, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"customer_id", type text}, {"customer_name", type text}, {"gender", type text}, {"age", Int64.Type}, {"city", type text}, {"state", type text}, {"customer_segment", type text}, {"onboarding_date", type date}, {"kyc_status", type text}}),
  #"Split column by delimiter" = Table.SplitColumn(#"Changed column type", "customer_name", Splitter.SplitTextByDelimiter(" "), {"firstName", "lastName"})
in
  #"Split column by delimiter";
shared Query_DataDestination = let
  Pattern = Fabric.Warehouse([CreateNavigationProperties = false, HierarchicalNavigation = true]),
  Navigation_1 = Pattern{[workspaceId = "."]}[Data],
  Navigation_2 = Navigation_1{[displayName = "vip_warehouse"]}[Data],
  Navigation_3 = Navigation_2{[Schema = "test"]}[Data],
  TableNavigation = Navigation_3{[Name = "customer_info"]}?[Data]?
in
  TableNavigation;
